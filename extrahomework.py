while True:
    def make_readable(seconds):
        h = seconds//3600
        m = (seconds-h*3600)//60
        s = seconds-(h*3600)-(m*60)
        print("%02d:%02d:%02d" % (h,m,s) if 0 < seconds <= 359999 else 'Время превышает допустимое значение или вы ввели отрицательное число!"')
    make_readable(int(input('enter seconds: ')))
