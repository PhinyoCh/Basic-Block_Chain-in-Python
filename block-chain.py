import datetime
import json
import hashlib
class Blockchain:
    def __init__(self): 
        #เก็บกลุ่มบล็อค
        self.chain = [] #list ที่ เก็บ Block
        #genesis block
        self.create_block(nonce=1, previous_hash="0")
        
    #สร้าง Block ขึ้นมาในระบบ Blockchain
    def create_block(self, nonce, previous_hash):
        #เก็บส่วนประกอบของ block แต่ละ Block
        block={
            "index" : len(self.chain) +1, #ID ของบล็อกที่สร้างขึ้นมา
            "timestamp" : str(datetime.datetime.now()), #วันเวลาที่สร้างบล็อคขึ้นมาในระบบ
            "nonce" : nonce, #ใช้เพื่อคำนวณ Minding
            "previous_hash" : previous_hash #ค่า hash ของบล็อคก่อนหน้า
        }
        self.chain.append(block)
        return block
    
    #ให้บริการเกี่ยวกับ Block ก่อนหน้า
    def get_previous_block(self):
        return self.chain[-1]

    #เข้ารหัส Block
    def hash(self, block):
        #แปลง Python Object (dict) => json object
        encode_block = json.dumps(block, sort_keys=True).encode()
        
        return hashlib.sha256(encode_block).hexdigest() #เข้ารหัสบล็อก เป็น sha-256 ในรูปแบบของ Hex
    
#ใช้งาน BlockChain
blockchain = Blockchain()
#เข้ารหัส Block แรก
print(blockchain.hash(blockchain.chain[0]))
#เข้ารหัส Block สอง
print(blockchain.hash(blockchain.chain[1]))