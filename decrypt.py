# import bcrypt

# # Generate a password hash
# # password = 'DSDG123'
# # retrieved_salt
# # salt = bcrypt.gensalt()
# # hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

# # # Store the hashed password and salt in the database
# # # ...

# # # To verify the password during login
# # entered_password = 'DSDG123'

# # # Retrieve the hashed password and salt from the database
# # # ...

# # # Hash the entered password with the retrieved salt
# # hashed_entered_password = bcrypt.hashpw(entered_password.encode('utf-8'), retrieved_salt)
# # print(hashed_password)
# # print(hashed_entered_password)
# # # Compare the hashed entered password with the stored hashed password
# # # if hashed_entered_password == retrieved_hashed_password:
# # #     # Passwords match
# # #     # Continue with the login process
# # # else:
# #     # Passwords do not match
# #     # Deny access



# import bcrypt
  
# # example password
# password = 'DSDG123'
  
# # converting password to array of bytes
# bytes = password.encode('utf-8')
  
# # generating the salt
# salt = bcrypt.gensalt()
  
# # Hashing the password
# hash = bcrypt.hashpw(bytes, salt)

# print(bcrypt.hashpw(password.encode('utf-8'),salt))
# print(hash)



# from passlib.hash import pbkdf2_sha256
# print(pbkdf2_sha256.hash("password", rounds=1024, salt=b'DSDG123'))
# print('pbkdf2_sha256$36000$0g4UW2KywxLN$gr6de6GpuWcU3lM3em3ATJ8YWQhboO3cR1XJua+yGFk=')

# from passlib.hash import pbkdf2_sha256
# from base64 import b64decode
# from passlib.utils.binary import ab64_encode

# def hashAndCompare(crackedHash):
    
#     crackedChain = crackedHash.split('$')   
#     #crackedChainDigest = crackedChain[0]
#     crackedChainRounds = crackedChain[1]
#     crackedChainSalt = crackedChain[2]
#     # crackedChainSaltPasslibFormat = ab64_encode(crackedChainSalt.encode('utf8')).decode('utf8')
#     # crackedChainHashData = crackedChain[3].split(':')
#     # crackedChainHash = crackedChainHashData[0]
#     # print(crackedChainHash)
#     # crackedChainHashPasslibFormat = ab64_encode(b64decode(crackedChainHash)).decode('utf8')
#     # print(crackedChainHashPasslibFormat)
#     # crackedChainData = crackedChainHashData[1]
#     # print(crackedChainData)
#     print(crackedChainSalt)
#     print(crackedChainSalt.encode('utf8').decode('utf-8'))
#     passlibHash = pbkdf2_sha256.hash('DSDG123', rounds=crackedChainRounds, salt=crackedChainSalt.encode('utf8')) 
#     passlibChain = passlibHash.split('$')
#     passlibChainSalt = passlibChain[3]
#     passlibChainHash = passlibChain[4]
#     print(ab64_encode(crackedChainSalt.encode('utf8')).decode('utf8'))
#     print(pbkdf2_sha256.hash('DSDG123'))
#     # print('Passlib: Hash: {0} Salt: {1}\nCracked: Hash: {2} Salt: {3}\n'.format(passlibChainHash, passlibChainSalt, crackedChainHashPasslibFormat, crackedChainSaltPasslibFormat))
#     print(passlibHash)
#     print('pbkdf2_sha256$36000$0g4UW2KywxLN$gr6de6GpuWcU3lM3em3ATJ8YWQhboO3cR1XJua+yGFk=')
# hashAndCompare('pbkdf2_sha256$36000$0g4UW2KywxLN$gr6de6GpuWcU3lM3em3ATJ8YWQhboO3cR1XJua+yGFk=:DSDG123')

# pbkdf2-sha256$36000$MGc0VVcyS3l3eExO$gr6de6GpuWcU3lM3em3ATJ8YWQhboO3cR1XJua.yGFk
# pbkdf2_sha256$36000$0g4UW2KywxLN$gr6de6GpuWcU3lM3em3ATJ8YWQhboO3cR1XJua+yGFk=

from passlib.hash import django_pbkdf2_sha256
hash = 'pbkdf2_sha256$36000$ZZoUXOsDWdjl$19qx7IXVSeZh+GKn7/Iaz2KHpg4DlkQCV1LW21pAWto='
user_input = 'ruchi@4'
print(django_pbkdf2_sha256.hash(user_input))
django_pbkdf2_sha256.verify(user_input, hash)
print(django_pbkdf2_sha256.verify(user_input, hash))

from passlib.apps import django_context
hash = 'pbkdf2_sha256$36000$ZZoUXOsDWdjl$19qx7IXVSeZh+GKn7/Iaz2KHpg4DlkQCV1LW21pAWto='
user_input = 'Ruchi@123'
print(django_context.hash(user_input))
django_context.verify(user_input, hash)
print(django_context.verify(user_input, hash))
# pbkdf2_sha256$36000$F3f9HPcQlHGG$TXyEW6gBABydj1wQUpwWlJZnO28fLZpzFeZDV/uDcUw=



# UPDATE `sister_site_db`.`sis_auth_customuser` SET `password` = 'pbkdf2_sha256$36000$0g4UW2KywxLN$gr6de6GpuWcU3lM3em3ATJ8YWQhboO3cR1XJua+yGFk=' WHERE (`email` = 'ruchi@gmail.com');
