
# yield 实现生产者-消费者模型

def customer():
    r = ''
    while True:
        n = yield r      # 这个r很关键，是生产者和消费者直接通信的桥梁，生产者发送信息和消费者返回信息都是由r承担
        if not n:
            return
        print('[CUSTOMER] customing #{}...'.format(n))
        r = '200 OK'

def producer(c):
    n = 1
    c.send(None)   # OR c.__next__()  启动生成器
    while n <= 10:
        print('[PRODUCER] producing #{}...'.format(n))
        r = c.send(n)
        print('[PRODUCER] Cutomer return - {}'.format(r))
        n += 1
    c.close()

if __name__ == '__main__':
    c = customer()
    producer(c)
