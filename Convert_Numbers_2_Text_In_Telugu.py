from Mappings import telugumap

numbers_Crores = ["కోటి"]

numbers_Lakhs = ["లక్ష"]

numbers_Thousands = ["వెయ్యి"]

numbers_Hundreds = ["వంద"]



def numbers_2_Telugu(num):
    k = 1000
    m = 10000
    b = 100000
    t = 10000000
    assert(0 <= num)
    if (num < 100):
        return telugumap[num]
    if (num < k):
        if num == 100: return numbers_Hundreds[0]
        elif num%100 ==0 and num>100:return telugumap[num // 100] +' '+ numbers_Hundreds[0]+'లు'
        else:
            if num<=199:
                return 'నూట '+ int_to_te(num % 100)
            else:
                return telugumap[num // 100] + ' వందల ' + int_to_te(num % 100)
    if (num<b):
        if num == k: return numbers_Thousands[0]
        elif num % k == 0 and num > k:
            return int_to_te(num // k) + ' వేలు'
        elif num>k and num<=1099:
            return 'వెయ్యిని '+ int_to_te(num % 100)
        elif num>=1100 and num <=1999:
            return  telugumap[num // 100] +' వందల '+ int_to_te(num % 100)
        elif num>=2000 and num<=99999:
            return int_to_te(num // k) + ' వేల ' + int_to_te(num % k)
    if (num < t):
        if num  == b: return 'ఒక ' + numbers_Lakhs[0]
        elif num%b== 0 and num > b: return int_to_te(num // b) + ' లక్షలు '
        elif num>b and num<=109999:
            return 'ఒక ' +numbers_Lakhs[0]+' '+ int_to_te(num % b)
        elif num>=110000 and num<=99999999:
            if num//b==1 and num>=b:
                return 'ఒక ' + numbers_Lakhs[0] +' '+ int_to_te(num % b)
            elif num>=120000 and num<1000000:
                return int_to_te(num // b) + ' లక్షల ' + int_to_te(num % b)
            elif num>=1000000 and num<t:
                return int_to_te(num // b) + ' లక్షల ' + int_to_te(num % b)
    if num == t:
        return 'ఒక '+numbers_Crores[0]

    raise AssertionError('num is too large: %s' % str(num))



print(numbers_2_Telugu(3))
