
import sqlite3

db = sqlite3.connect('Assets.db')

cursor = db.cursor()

cursor.execute("CREATE TABLE  assets (id INTEGER PRIMARY KEY, Name TEXT, Price INTEGER , Count INTEGER)")

#INSERT

id = '3'
Name = 'Apartment'
Price= '800'
Count = '1'

cursor.execute(''' INSERT INTO assets(id,Name,Price,Count) VALUE(?,?,?,?) ''' ,(id, Name,Price,Count))

db.commit()

#UPDATE

newprice1 = '1300'
newprice3 = '200'
assets_id1 = '1'
assets_id3 = '3'

cursor.execute('''UPDATE assets SET Price = ? WHERE id = ?''',(newprice1 , assets_id1))

cursor.execute('''UPDATE assets SET Price = ? WHERE id = ?''',(newprice3 , assets_id3))

#DELETE & INSERT

delete_id = '3'
delete_id = '2'

new_id = '4'
new_name = 'Money'
new_price = '10'
new_count = '60'

cursor.execute('''DELETE FROM assets WHERE id = ?''',(delete_assets_id = '3',))

cursor.execute('''DELETE FROM assets WHERE id = ?''',(delete_assets_id = '2',))

cursor.execute(''' INSERT INTO assets(id,Name,Price,Count) VALUE(?,?,?,?) ''' ,(new_id , new_name,new_price,new_count)

db.commit()

#INSERT & UPDATE

new_id1 = '5'
new_name1 = 'EOS'
new_price1 = '40'
new_count1 = '5'

new_assets_id2 = '6'
new_name2 = 'ETH'
new_price2 = '7'
new_count2 = '60'

new_count4 = '25 '
assets_id4 = '4'

cursor.execute(''' INSERT INTO assets(id,Name,Price,Count) VALUE(?,?,?,?) ''' ,(new_id1 , new_name1,new_price1,new_count1)

cursor.execute(''' INSERT INTO assets(id,Name,Price,Count) VALUE(?,?,?,?) ''' ,(new_id2 , new_name2,new_price2,new_count2)

cursor.execute('''UPDATE assets SET Count = ? WHERE id = ?''',(new_count4 , assets_id4))

db.commit

cursor.execute('''SELECT Name,Price,Count FROM assets''')
print(cursor.fetchall())

db.commit()
db.close()