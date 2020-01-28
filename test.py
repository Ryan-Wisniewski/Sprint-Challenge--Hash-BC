st = 'abcdefghijklmnop'

print(st[:6])
#from end
print(st[-6:])

last_hash = 'd01f4f84e7ea904b52c1345fc4a8bea269ee5b31bc7d33afcbbd4ec9522a1021'
new_hash = '2a1021fa4a9aa1f9559c6574b54543c8b9f236727db47bcc0cefc70bb2567e89'

print(len(last_hash))
print(len(new_hash))

if last_hash[-6:] == new_hash[:6]:
    print('bishhhhhhhh work')

print(last_hash[-6:])
print(new_hash[:6])