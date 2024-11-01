"""class practice"""


# Create class
class Profile:
    # define attributes with types
    username: str
    followers: list[str]
    following: list[str]

    # initialize when object is created
    def __init__(self, handle: str):
        self.username = handle
        self.followers = []
        self.following = []

    # define meathods
    def follow(self, username: str) -> None:
        self.following.append(username)

    def following_count(self) -> int:
        return len(self.following)


# Create object of tuype Profile
my_prof: Profile = Profile("comp110fan")
# Call meathod in function
my_prof.follow("unc.latinosintech")
print(my_prof.following_count())
