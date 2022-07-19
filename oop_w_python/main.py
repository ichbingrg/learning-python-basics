from user import User
from post import Post

user1 = User("sudip", "sudip@mail.com", "OMGPASSWORD", "Working Student")
user2 = User("someone", "someone@gmx.de", "secret", "Agent")

user1.get_user_info()
user2.get_user_info()

post1 = Post("Feeling really good in germany", user2)
post1.get_post_info()