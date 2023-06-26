import pandas as pd
from model.config import engine

# puma
# sql语句
sql = "SELECT * FROM jdspider.jd_comment  WHERE product_id='67309469981' ORDER BY creationTime DESC LIMIT 50"
sql1 = "SELECT * FROM jdspider.jd_comment  WHERE product_id='67309469981'"
sql2 = "SELECT text FROM jdspider.emotional  WHERE product_id='67309469981' AND emotional='正面'"
sql3 = "SELECT text FROM jdspider.emotional  WHERE product_id='67309469981' AND emotional='负面'"
# 通过pandas读取数据
puma = pd.read_sql(sql, engine)
puma1 = pd.read_sql(sql1, engine)
puma2 = pd.read_sql(sql2, engine)
puma3 = pd.read_sql(sql3, engine)

# adidas
# sql语句
sql = "SELECT * FROM jdspider.jd_comment  WHERE product_id='100018065813' ORDER BY creationTime DESC LIMIT 50"
sql1 = "SELECT * FROM jdspider.jd_comment  WHERE product_id='100018065813'"
sql2 = "SELECT text FROM jdspider.emotional  WHERE product_id='100018065813' AND emotional='正面'"
sql3 = "SELECT text FROM jdspider.emotional  WHERE product_id='100018065813' AND emotional='负面'"
# 通过pandas读取数据
adidas = pd.read_sql(sql, engine)
adidas1 = pd.read_sql(sql1, engine)
adidas2 = pd.read_sql(sql2, engine)
adidas3 = pd.read_sql(sql3, engine)

# nike
# sql语句
sql = "SELECT * FROM jdspider.jd_comment  WHERE product_id='100015163119' ORDER BY creationTime DESC LIMIT 50"
sql1 = "SELECT * FROM jdspider.jd_comment  WHERE product_id='100015163119'"
sql2 = "SELECT text FROM jdspider.emotional  WHERE product_id='100015163119' AND emotional='正面'"
sql3 = "SELECT text FROM jdspider.emotional  WHERE product_id='100015163119' AND emotional='负面'"
# 通过pandas读取数据
nike = pd.read_sql(sql, engine)
nike1 = pd.read_sql(sql1, engine)
nike2 = pd.read_sql(sql2, engine)
nike3 = pd.read_sql(sql3, engine)

# 斯凯奇Skechers
# sql语句
sql = "SELECT * FROM jdspider.jd_comment  WHERE product_id='100017977183' ORDER BY creationTime DESC LIMIT 50"
sql1 = "SELECT * FROM jdspider.jd_comment  WHERE product_id='100017977183'"
sql2 = "SELECT text FROM jdspider.emotional  WHERE product_id='100017977183' AND emotional='正面'"
sql3 = "SELECT text FROM jdspider.emotional  WHERE product_id='100017977183' AND emotional='负面'"
# 通过pandas读取数据
Skechers = pd.read_sql(sql, engine)
Skechers1 = pd.read_sql(sql1, engine)
Skechers2 = pd.read_sql(sql2, engine)
Skechers3 = pd.read_sql(sql3, engine)

# anta
# sql语句
sql = "SELECT * FROM jdspider.jd_comment  WHERE product_id='10038719197887' ORDER BY creationTime DESC LIMIT 50"
sql1 = "SELECT * FROM jdspider.jd_comment  WHERE product_id='10038719197887'"
sql2 = "SELECT text FROM jdspider.emotional  WHERE product_id='10038719197887' AND emotional='正面'"
sql3 = "SELECT text FROM jdspider.emotional  WHERE product_id='10038719197887' AND emotional='负面'"
# 通过pandas读取数据
anta = pd.read_sql(sql, engine)
anta1 = pd.read_sql(sql1, engine)
anta2 = pd.read_sql(sql2, engine)
anta3 = pd.read_sql(sql3, engine)

# peak
# sql语句
sql = "SELECT * FROM jdspider.jd_comment  WHERE product_id='100010012807' ORDER BY creationTime DESC LIMIT 50"
sql1 = "SELECT * FROM jdspider.jd_comment  WHERE product_id='100010012807'"
sql2 = "SELECT text FROM jdspider.emotional  WHERE product_id='100010012807' AND emotional='正面'"
sql3 = "SELECT text FROM jdspider.emotional  WHERE product_id='100010012807' AND emotional='负面'"
# 通过pandas读取数据
peak = pd.read_sql(sql, engine)
peak1 = pd.read_sql(sql1, engine)
peak2 = pd.read_sql(sql2, engine)
peak3 = pd.read_sql(sql3, engine)

# asics
# sql语句
sql = "SELECT * FROM jdspider.jd_comment  WHERE product_id='10025818742036' ORDER BY creationTime DESC LIMIT 50"
sql1 = "SELECT * FROM jdspider.jd_comment  WHERE product_id='10025818742036'"
sql2 = "SELECT text FROM jdspider.emotional  WHERE product_id='10025818742036' AND emotional='正面'"
sql3 = "SELECT text FROM jdspider.emotional  WHERE product_id='10025818742036' AND emotional='负面'"
# 通过pandas读取数据
asics = pd.read_sql(sql, engine)
asics1 = pd.read_sql(sql1, engine)
asics2 = pd.read_sql(sql2, engine)
asics3 = pd.read_sql(sql3, engine)

# NEWBALANCE
# sql语句
sql = "SELECT * FROM jdspider.jd_comment  WHERE product_id='10034116992996' ORDER BY creationTime DESC LIMIT 50"
sql1 = "SELECT * FROM jdspider.jd_comment  WHERE product_id='10034116992996'"
sql2 = "SELECT text FROM jdspider.emotional  WHERE product_id='10034116992996' AND emotional='正面'"
sql3 = "SELECT text FROM jdspider.emotional  WHERE product_id='10034116992996' AND emotional='负面'"
# 通过pandas读取数据
new = pd.read_sql(sql, engine)
new1 = pd.read_sql(sql1, engine)
new2 = pd.read_sql(sql2, engine)
new3 = pd.read_sql(sql3, engine)

# other
# sql语句
# sql = "SELECT * FROM jdspider.jd_comment  WHERE product_id='' ORDER BY creationTime DESC LIMIT 50"
# sql1 = "SELECT * FROM jdspider.jd_comment  WHERE product_id=''"
# sql2 = "SELECT text FROM jdspider.emotional  WHERE product_id='' AND emotional='正面'"
# sql3 = "SELECT text FROM jdspider.emotional  WHERE product_id='' AND emotional='负面'"
# 通过pandas读取数据
# other = pd.read_sql(sql, engine)
# other1 = pd.read_sql(sql1, engine)
# other2 = pd.read_sql(sql2, engine)
# other3 = pd.read_sql(sql3, engine)
