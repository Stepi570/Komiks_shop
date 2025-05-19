import psycopg2
from config import db_name,host,password,user

def sql(text):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            sslrootcert="/etc/ssl/certs/ca-certificates.crt"
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(text)
            
            if cursor.description:
                result = cursor.fetchall()
                # Если в результате один столбец — преобразуем в плоский список
                if len(cursor.description) == 1:
                    return [row[0] for row in result]  # Пример: [0, 1, 2]
                else:
                    return result  # Пример: [(0, "Ivan"), (1, "Anna")]
            else:
                return cursor.rowcount  # Для INSERT/UPDATE/DELETE
            
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    finally:
        if connection:
            connection.close()
            print("Соединение закрыто")


def newtabl():
    h="CREATE TABLE users (id BIGINT PRIMARY KEY,username VARCHAR(30), balance BIGINT)"
    sql(h)
    h="CREATE TABLE komiks (id SERIAL PRIMARY KEY ,name VARCHAR(100),info VARCHAR(1000),photo_name VARCHAR(200), state VARCHAR(100), avtor_id BIGINT,donate VARCHAR(300),price INTEGER)"
    sql(h)
    h="CREATE TABLE subscribe (subscribe_id SMALLINT,user_id BIGINT)"
    sql(h)
    h="CREATE TABLE glavs (id_komiks SMALLINT,number_glavs SMALLINT,file_id VARCHAR(300), price INTEGER)"
    sql(h)
    h="CREATE TABLE otziv (user_id BIGINT,komiks_id INTEGER,glav VARCHAR(50),stars INTEGER,text VARCHAR(6000))"
    sql(h)
    h="CREATE TABLE transaction (chek VARCHAR(300) , date VARCHAR(30), user_id BIGINT, money BIGINT, info VARCHAR(300), komiks_id VARCHAR(30))"
    sql(h)

def findpiple(id):
    h=f"SELECT * FROM users WHERE  id = {id}"
    return (sql(h))

def new_pipl(id,us,balance):
    h=f"INSERT INTO users (id, username, balance) VALUES ({id},'{us}',{balance})"
    return ((sql(h)))

def all_people_id():
    h="SELECT id FROM users"
    return ((sql(h)))

def all_people_username():
    h="SELECT username FROM users"
    return ((sql(h)))

def new_komiks(name,info,photo_name,avtor_id,donate,price):
    h=f"INSERT INTO komiks (name,info,photo_name,avtor_id,state,donate,price) VALUES ('{name}','{info}','{photo_name}',{avtor_id},'в написании','{donate}',{price})"
    return ((sql(h)))

def spisok_komic(stolbech):
    h=f"SELECT {stolbech} FROM komiks"
    x = sql(h)
    if x==[]:
        return 0
    with open("komiks.txt", 'a') as file:
        try:
            for i in range(len(x)):
                file.write(f"{') '.join(map(str, x[i]))}")
        except:
            file.write(f"{') '.join(map(str, x))}")
    return 1
    
def delete_komiks(number):
    h=f"DELETE FROM komiks WHERE id={number};"
    return ((sql(h)))

def spisok_komic2(stolbech):
    h=f"SELECT {stolbech} FROM komiks"
    return sql(h)

def one_info(stolbech,where):
    h=f"SELECT {stolbech} FROM komiks WHERE {where}"
    return sql(h)

def new_subscribe(sb_id,id):
    h=F"INSERT INTO subscribe (subscribe_id,user_id) VALUES ({sb_id},{id})"
    return sql(h)

def chek_subscribe(sb_id,id):
    h=f"SELECT * FROM subscribe WHERE subscribe_id={sb_id} AND user_id={id}"
    return sql(h)

def delete_subscribe(sb_id,id):
    h=f"DELETE FROM subscribe WHERE subscribe_id={sb_id} AND user_id={id}"
    return sql(h)

def count_glavs(number):
    h=F"SELECT number_glavs FROM glavs WHERE id_komiks={number} ORDER BY number_glavs ASC"
    return sql(h)

def new_glav(id_kom,num_glav,file_id,price):
    h=F"INSERT INTO glavs (id_komiks,number_glavs,file_id, price) VALUES ({id_kom},{num_glav},'{file_id}',{price})"
    return sql(h)

def glavs(number):
    h=f"SELECT * FROM glavs WHERE id_komiks={number} ORDER BY number_glavs ASC"
    return sql(h)

def file_glavs(num,glav):
    h=f"SELECT file_id FROM glavs WHERE id_komiks={num} AND number_glavs={glav}"
    return sql(h)

def change(num,glav,file_id):
    h=F"UPDATE glavs SET file_id = '{str(file_id)}' WHERE id_komiks={num} AND number_glavs={glav}"
    return sql(h)

def new_otziv(user,komiks,glav,stars,text):
    h=f"INSERT INTO otziv (user_id ,komiks_id ,glav ,stars ,text) VALUES ({user},{komiks},'{glav}',{stars},'{text}')"
    return sql(h)

def reiting(id):
    h=f"SELECT stars FROM otziv WHERE komiks_id={id}"
    return sql(h)

def find():
    h=f"SELECT name,id FROM komiks"
    return sql(h)

def my_subskr(id):
    h=f"SELECT * FROM (SELECT a.user_id,b.name, b.id FROM subscribe AS a INNER JOIN komiks AS b ON a.subscribe_id=b.id) WHERE user_id={id}"
    return sql(h)

def my_otzivs(id):
    h=f"SELECT a.komiks_id,a.glav,a.text,b.name , a.stars FROM otziv AS a INNER JOIN komiks AS b ON a.komiks_id = b.id WHERE a.user_id={id}"
    return sql(h)

def delit_otziv(id,glav,user_id):
    h=f"DELETE FROM otziv WHERE user_id={user_id} AND komiks_id={id} AND glav='{glav}'"
    return sql(h)

def glav_chek(user_id,kom_id,glav_id):
    h=f"SELECT * FROM otziv WHERE user_id={user_id} AND komiks_id={kom_id} AND glav='{glav_id}'"
    return sql(h)

def replase_info(stolb,new_info,kom):
    h=f"UPDATE komiks SET {stolb}='{new_info}' WHERE id={kom}"
    return sql(h)

def spisok_glav(id):
    h=f"SELECT number_glavs FROM glavs WHERE id_komiks={id} ORDER BY number_glavs ASC"
    return sql(h)

def delete_glav(kom,glav):
    h=f"DELETE FROM glavs WHERE id_komiks={kom} AND number_glavs={glav}"
    return sql(h)

def countt(stolb,table,uslovie):
    h=f"SELECT COUNT({stolb}) FROM {table} WHERE {uslovie}"
    return sql(h)

def chek_balance(id):
    h=f"SELECT balance FROM users WHERE id={id}"
    return sql(h)

def delete(table,uslovie):
    h=f"DELETE FROM {table} WHERE {uslovie}"
    return sql(h)

def all_otzivs(id):
    h=f"SELECT a.glav,a.stars,a.text,b.username, b.id FROM otziv AS a INNER JOIN users AS b ON a.user_id=b.id WHERE a.komiks_id={id}"
    return sql(h)

def statistik_users(stolbech):
    h=f"SELECT {stolbech} FROM users"
    x = sql(h)
    if x==[]:
        return 0
    with open("users.txt", 'a') as file:
        for i in x:
            file.write(f"Имя: {"Отсутствует" if i[1]=="None" else f"@{i[1]}"} ID: {i[0]} Баланс: {i[2]} ₽\n")
    return 1

def user_money(id):
    h=f"SELECT balance FROM users WHERE id={id}"
    return sql(h)

def change_balance(user,money):
    h=f"UPDATE users SET balance={money} WHERE id={user}"
    return sql(h)

def transaktion(tr_id,date,user_id,money,info,komiks_id):
    h=f"INSERT INTO transaction (chek , date , user_id , money , info,komiks_id) VALUES ('{tr_id}','{date}',{user_id},{money},'{info}',{komiks_id})"
    return sql(h)

def chek_pokupki(user_id,komiks_id):
    h=f"SELECT * FROM transaction WHERE user_id={user_id} AND komiks_id='{komiks_id}'"
    return sql(h)

def chek_priсу(komiks_id,glav):
    h=f"SELECT price FROM glavs WHERE id_komiks={komiks_id} AND number_glavs='{glav}'"
    return sql(h)

def hostory_pokupok(user_id):
    h=f"SELECT chek , date , money, info FROM transaction WHERE user_id={user_id}"
    return sql(h)

def change_prise(table,new_prise,uslovia):
    h=f"UPDATE {table} SET {new_prise} WHERE {uslovia}"
    return sql(h)

def chek_transaktion(chek):
    h=f"SELECT chek , date , money, info FROM transaction WHERE chek='{chek}'"
    return sql(h)

def all_transaktion():
    h=f"SELECT chek , date , money, info FROM transaction"
    return sql(h)
