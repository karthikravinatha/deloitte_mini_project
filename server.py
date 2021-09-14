from fastapi import FastAPI
import sqlite3
app = FastAPI()


'''
all methods are connected to the database
according to the url specific navigation of
data flow will happens.
'''
@app.get("/get_blogs")
async def get_blogs():
    #database connection happens here
    conn = sqlite3.connect("mini.db")
    cur = conn.execute("SELECT * FROM metrics")
    blogs = cur.fetchall()
    blogs_json = []
    for each in blogs:
        single_blog = {}
        single_blog['id'] = each[0]
        single_blog['user_id'] = each[1]
        single_blog['assignmant_code'] = each[2]
        single_blog['deployment_url'] = each[3]
        single_blog['code_quality_rating'] = each[4]
        single_blog['code_coverage'] = each[5]
        single_blog['quiz_score'] = each[6]
        blogs_json.append(single_blog)
    return blogs_json

@app.get("/get_by_user")
async def get_by_user(id):
    conn = sqlite3.connect("mini.db")
    sql = "SELECT * FROM metrics WHERE id=%s" % id
    cur = conn.execute(sql)
    data = cur.fetchall()
    data_json = []
    for i in data:
        single_blog = {}
        single_blog['id'] = i[0]
        single_blog['user_id'] = i[1]
        single_blog['assignmant_code'] = i[2]
        single_blog['deployment_url'] = i[3]
        single_blog['code_quality_rating'] = i[4]
        single_blog['code_coverage'] = i[5]
        single_blog['quiz_score'] = i[6]
        data_json.append(single_blog)
    return data_json

@app.post("/add")
async def add(user_id,assignmant_code,deployment_url,code_quality_rating,code_coverage,quiz_score):
    conn = sqlite3.connect("mini.db")
    sql = "INSERT INTO metrics(user_id,assignmant_code,deployment_url,code_quality_rating,code_coverage,quiz_score) VALUES ('%s','%s','%s','%s','%s','%s')" % (user_id,assignmant_code,deployment_url,code_quality_rating,code_coverage,quiz_score)
    conn.execute(sql)
    conn.commit()
    conn.close()

@app.post("/delete")
async def delete(id):
    conn = sqlite3.connect("mini.db")
    sql = "DELETE FROM metrics WHERE id=%s" % id
    conn.execute(sql)
    conn.commit()
    conn.close()

@app.post("/update")
async def update(id,url,rating,coverage,quiz_score):
    conn = sqlite3.connect("mini.db")
    sql = "UPDATE metrics SET deployment_url='%s', code_quality_rating='%s', code_coverage='%s', quiz_score='%s' WHERE id=%s" % (url,rating,coverage,quiz_score,id)
    conn.execute(sql)
    conn.commit()
    conn.close()

@app.post("/user_add")
async def user_add(name,phone,email,is_delete):
    conn = sqlite3.connect("test.db")
    sql = "INSERT INTO user(name,phone_no,email,is_delete) VALUES ('%s','%s','%s','%s')" % (name,phone,email,is_delete)
    conn.execute(sql)
    conn.commit()
    conn.close()


@app.post("/user_update")
async def update(id,name,phone,email,is_delete):
    conn = sqlite3.connect("mini.db")
    sql = "UPDATE metrics SET name='%s', phone_no='%s', email='%s', is_delete='%s' WHERE id=%s" % (name,phone,email,is_delete,id)
    conn.execute(sql)
    conn.commit()
    conn.close()

@app.post("/user_delete")
async def user_delete(id):
    conn = sqlite3.connect("mini.db")
    sql = "DELETE FROM user WHERE id=%s" % id
    conn.execute(sql)
    conn.commit()
    conn.close()

@app.post("/add_tags")
async def add_tags(name):
    conn = sqlite3.connect("test.db")
    sql = "INSERT INTO tags(name) VALUES ('%s')" % (name)
    conn.execute(sql)
    conn.commit()
    conn.close()

@app.post("/tags_delete")
async def user_delete(id):
    conn = sqlite3.connect("mini.db")
    sql = "DELETE FROM tagsw WHERE id=%s" % id
    conn.execute(sql)
    conn.commit()
    conn.close()
