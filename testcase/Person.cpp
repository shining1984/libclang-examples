//
//This testcase come from the blog:
//http://eli.thegreenplace.net/2011/07/03/parsing-c-in-python-with-clang/comment-page-1/#comment-1372238
//
class Person {
};


class Room {
public:
    void add_person(Person person)
    {
        // do stuff
    }

private:
    Person* people_in_room;
};


template <class T, int N>
class Bag<T, N> {
};


int main()
{
    Person* p = new Person();
    Bag<Person, 42> bagofpersons;

    return 0;
}
