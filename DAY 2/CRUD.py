#tuple hold user, list hold post, validate, allow users to create, read, delete

users = ('Tope' , 'Femi', 'Kunle', 'Mayowa')
posts = ['Ill make lunch','I need to rest','Visiting paris','Just wedded','Anticipating Christmas']

new_user = str(input("Enter your username: "))
if new_user not in users :
    print ("Invalid user")
else : 
    print("Welcome, " + new_user + " what operation do you want to peform")
    print()
    print("1. Create post")
    print("2. Read post")
    print("3. Delete post")
    print("4. Update post")
    operation = int(input("Enter the position of operation you want to perform: "))

        #add post
    if operation == 1 :
        new_post = str(input("Enter new post: "))
        posts.append(new_post)
        print("----Post added successfully----")
        print(posts)
        # read post
    elif operation == 2 :
        print("---List of Posts---")
        for element in posts:
            print(element)
        #Delete post
    elif operation == 3 :
        print("Current posts: " + str(posts))
        print("--Delete post---")
        post_to_delete = str(input("Enter post to delete "))
        posts.remove(post_to_delete)
        print("---Post deleted successfully---")
        print(posts)
        #Update post
    elif operation == 4 :
        print("----Available Post----")
        i = 1
        while i < len(posts) :
            for post in posts :
                print(str(i) + ". " + post)
                i += 1
        print()
        post_to_update = int(input("Enter id of post to delete: "))
        post_new_version = str(input("Enter new post: "))

        posts.pop(post_to_update - 1)
        posts.insert(post_to_update - 1, post_new_version)  #UPDATE LIST
        for post in posts :  print(post)
#delete post
        i = 0
        while i <= len(posts):
             for post in posts:
                i +=1
                print(str(i) + str(posts))
         
        post_to_delete = int(input("Enter id of post to delete e.g 4"))
        try :
            print("----post deleted successfully")
            print(posts.pop(post_to_delete))
        except Exception as e:
            print(str(e))
   
    else :
        print("Enter a valid operation")


    
   
