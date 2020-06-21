import sys, os
from skillshare import Skillshare
from magic import cookie

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


def info():
    print(r"""

                      __________                               
                      \______   \ ______  _  _______________   
                      |       _// __ \ \/ \/ /\___   /\__  \  
                      |    |   \  ___/\     /  /    /  / __ \_
                      |____|___/\_____>\/\_/  /______\(______/        

        	 
                                                  


				Tel: t.me/PyC0der

                """)


if __name__ == "__main__":
    info()
    main()
