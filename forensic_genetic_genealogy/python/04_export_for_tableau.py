import os
import pandas as pd
from db_connect import get_connection

# Output folder for Tableau-ready CSVs
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "processed")
os.makedirs(OUT_DIR, exist_ok=True)

conn = get_connection()
ss


# 1) Cluster summary
cluster_summary = pd.read_sql_query("""
SELECT
  cluster_id,
  COUNT(*) AS cluster_size
FROM match_clusters
GROUP BY cluster_id
ORDER BY cluster_size DESC;
""", conn)
cluster_summary.to_csv(os.path.join(OUT_DIR, "cluster_summary.csv"), index=False)

# 2) Match strength by cluster
match_strength = pd.read_sql_query("""
SELECT
  mc.cluster_id,
  m.match_id,
  m.cm_total,
  m.segments,
  m.longest_segment,
  m.tree_confidence
FROM match_clusters mc
JOIN matches m ON m.match_id = mc.match_id;
""", conn)
match_strength.to_csv(os.path.join(OUT_DIR, "match_strength_by_cluster.csv"), index=False)

# 3) Top surnames per cluster (top 25)
top_surnames = pd.read_sql_query("""
SELECT
  cluster_id,
  last_name,
  surname_count,
  avg_link_conf
FROM (
  SELECT
    cluster_id,
    last_name,
    surname_count,
    avg_link_conf,
    ROW_NUMBER() OVER (PARTITION BY cluster_id ORDER BY surname_count DESC) AS rn
  FROM (
    SELECT
      mc.cluster_id,
      p.last_name,
      COUNT(*) AS surname_count,
      AVG(l.confidence_level) AS avg_link_conf
    FROM match_clusters mc
    JOIN match_tree_links l ON l.match_id = mc.match_id
    JOIN persons p ON p.person_id = l.person_id
    WHERE p.last_name IS NOT NULL AND TRIM(p.last_name) <> ''
    GROUP BY mc.cluster_id, p.last_name
  )
)
WHERE rn <= 25
ORDER BY cluster_id, surname_count DESC;
""", conn)
top_surnames.to_csv(os.path.join(OUT_DIR, "top_surnames_by_cluster.csv"), index=False)

# 4) Louisiana geo hotspots by cluster
la_geo = pd.read_sql_query("""
SELECT
  mc.cluster_id,
  pl.state,
  pl.parish_or_county,
  pl.place_name,
  pl.lat,
  pl.lon,
  COUNT(*) AS people_count
FROM match_clusters mc
JOIN match_tree_links l ON l.match_id = mc.match_id
JOIN persons p ON p.person_id = l.person_id
JOIN places pl ON pl.place_id = p.place_id_birth
WHERE pl.state = 'LA'
GROUP BY mc.cluster_id, pl.state, pl.parish_or_county, pl.place_name, pl.lat, pl.lon
ORDER BY mc.cluster_id, people_count DESC;
""", conn)
la_geo.to_csv(os.path.join(OUT_DIR, "la_geo_by_cluster.csv"), index=False)

# 5) Candidate rankings (from your scoring model)
candidate_rankings = pd.read_sql_query("""
SELECT *
FROM candidate_rankings
ORDER BY candidate_score DESC;
""", conn)
candidate_rankings.to_csv(os.path.join(OUT_DIR, "candidate_rankings.csv"), index=False)

conn.close()

print("\n✅ Tableau exports written to:")
print(os.path.abspath(OUT_DIR))
print("\nFiles created:")
for f in [
    "cluster_summary.csv",
    "match_strength_by_cluster.csv",
    "top_surnames_by_cluster.csv",
    "la_geo_by_cluster.csv",
    "candidate_rankings.csv",
]:
    print(" -", f)

