#define debază main //codul
#define cațâșt cout //print
#define caintro cin //input
#define arăt ptr //pointer e un arătător
//Asm// It is used to declare a block of code that has to be passed to the assembler.
//auto// This keyword is a storage class specifier that is used for defining objects in a particular block.
#define rupe break// This statement terminates any switch statement or any loop.
#define caz case // This keyword is used specifically within a switch statement to specify a match for the expression of the statement.
#define prinde catch// It specifies which actions have to be taken when an exception occurs.
#define caract char// This is one of the fundamental data types in C++ language that defines character objects.
#define clasa class// It is used to declare a user-defined data type that encapsulates any data members and operations or member functions of a particular class.
// #define const This keyword helps to define objects whose value will not alter throughout the lifetime of execution of that particular program.
// continue// It transfers control to the starting point of a loop.
#define implicit default// This keyword handles expression values in a switch statement that could not be handled by case.
#define ștergere delete// It is a memory deallocation operator.
#define fă do// indicate the start of a do-while statement in which the sub-statement is executed repeatedly until the value of the expression is logical-false.
#define dublu double// Fundamental data type used to define a floating-point number.
#define altfel else// Used specifically in an if-else statement.
// enum// To declare a user-defined enumeration data type.
// extern// An identifier specified as an extern has an external linkage to the block.
#define fluct float// Fundamental data type used to define a floating-point number.
#define pentru for// Indicates the start of a statement to achieve repetitive control.
#define prieten friend// A class or operation whose implementation can access the private data members of a class.
#define lung long// A data type modifier that defines a 32-bit int or an extended double.
#define nou new// Memory allocation operator.
// operator// Overloads a C++ operator with a new declaration.
// private// Declares class members who are not visible outside the class.
#define protejat protected// Declares class members who are private except to derived classes
// public// Declares class members who are visible outside the class.
#define registru register//A storage class specifier that is an auto specifier, but which also indicates to the compiler that an object will be frequently used and should therefore be kept in a register.
#define dutela goto// This keyword helps to transfer the power of the control to a specified label.
#define dacă if// It indicates the starting point of an if statement to achieve selective control.
#define înlinie inline// A function specifier that indicates to the compiler that inline substitution of the function body is to be preferred to the usual function call implementation.
// int// fundamental data type used to define integer objects.
// define return// Returns an object to a function’s caller.
#define scurt short// A data type modifier that defines a 16-bit int number.
#define semnat signed// A data type modifier that indicates an object’s sign is to be stored in the high-order bit.
#define mărimea sizeof// Returns the size of an object in bytes.
// static// The lifetime of an object-defined static exists throughout the lifetime of program execution.
// struct// To declare new types that encapsulate both data and member functions.
#define înlocuire switch// This keyword is used in the switch statement.
#define șablon template// parameterized or generic type.
#define asta this// A class pointer points to an object or instance of the class.
#define aruncă throw// Generate an exception.
#define încearcă try// Indicates the start of a block of exception handlers.
#define tipărdef typedef// Synonym for another integral or user-defined type.
#define uniune union// Similar to a structure, struct, in that it can hold different types of data, but a union can hold only one of its members at a given time.
#define nesemnat unsigned// A data type modifier that indicates the high-order bit is to be used for an object.
// define virtual// A function specifier that declares a member function of a class that will be redefined by a derived class.
#define vid void// This keyword identifies the absence of a type or function parameter list.
// define volatile// This particular keyword defines an object that may vary in value in a way that is undetectable to the compiler.
#define câtimp while// This keyword helps to start a while statement and end a do...whileloop.
//cos() Returns Cosine of the Argument
// sin() Returns Sine of the Argument
// asin() Returns Inverse Sine a Number
// atan() Returns Inverse tangent a Number
// tan() Returns Tangent of the Argument
// atan2() Returns Inverse Tangent of a Coordinate
// acos() Returns Inverse cosine a Number
#define plafon ceil() //Return ceiling value of number
#define podea floor() //Returns floor value of decimal number
// fmod() Computes floating point remainder of division
// log() Returns Natural Logarithm of a Number
// trunc() Truncates the demical part of a number
#define rotunjire round() //Returns integral value nearest to argument
// log10() Returns Base 10 Logarithm of a Number
// modf() Breaks Number Into Integral and Fractional Part
// exp() returns exponential (e) raised to a number
// log2() returns base2 logarithm of a number
#define radicpătr sqrt() //Computes Square Root of A Number
// fmax() //returns largest among two arguments passed
// cmath abs() Returns absolute value of an argument
// nan() //returns a quiet NaN value ==non-număr
// fabs() //Returns absolute value of argument
#define rămășițaremainder() //Returns remainder of x/y
#define putere pow() //Computes Power a Number
// <cstdlib>
#define asciiînfluct atof() // Converts String to Double (ASCII to float)
#define șrgînl strtol() //Converts a string to long integer number
#define șrgînnesemnl strtoull() //converts string to unsigned long long int
#define semănarand srand() //Seeds pseudo random number for rand()
#define eliberare free() //deallocates a block of memory
// malloc() //Allocates a block of unitialized memory
// realloc() //reallocates a block of previously allocated memory
#define luarenv getenv() //returns pointer to environment variable passed
#define bcăutare bsearch() //performs binary search on sorted array
#define iutesort qsort() //sorts array using quick-sort algorithm
//cstdlib
// abs() //Returns absolute value of an integer
// div() //computes integral quotient and remainder of number
// labs() //returns absolute value of long or long int number
// calloc() //allocates block of memory and initializes to zero
// <iostream>
// cerr //Writes to error stream
// clog //used for streaming logs
#define lwintrocin //accepts input in wide character type(lăcrat/lungit))
#define lcațâșt wcout //displays wide characters (Unicode) to screen
// <cstring>
// memcpy() // Copies block of memory from source to destination
#define șrgcpi strncpy() //copies character string from source to destination
#define șrgconcat strcat() //appends copy of string to end of another string
#define șrgcaractcpi strcpy() //Copies character string from source to destination
#define șrgcmp strcmp() //Compare two strings
#define șrgcmplex strncmp() //compares two strings lexographically
#define șrgcaractcăut strchr() //searches for character in string
#define șrgsubșrg strstr() //finds first occurrence of a substring in string
#define șrgtok strtok() //Split string based on delimiter
//  memset() //copies character to beginning of string n times
#define șrglung strlen() //Returns length of given string
// <cctype>
#define îialfa isalpha() //checks if given character is alphabet or not
#define îicifră isdigit() //Checks if given character is a digit or not
#define îiblanc isblank() //checks if given character is a blank character
#define îimajusc isupper()
#define îiminusc islower() //checks if given character is lowercase
#define îipunct ispunct() //check if given character is punctuation character
#define îispațiu isspace() //check if given character is whitespace character
#define îisuper isupper() //check if given character is uppercase or not
#define îihexcifră isxdigit() //checks if given character is hexadecimal character
#define înminusc tolower() //Converts a given character to lowercase
#define înmajusc toupper() //Converts a given character to uppercase
// <cstdio>
#define tmpfișier tmpfile() //creates temporary file with auto-generated name
#define scoate remove() //Deletes the specified file
#define renumire rename() //renames or moves specified file
#define găsdeschiderefopen() //opens specified file
// scanf() //Read data form stdin//
// fprintf() write a formatted string to file stream///
// fscanf() // read data from file stream///
// printf() Write formatted string to stdout
// snprintf() write formatted string to character string buffer
// sprintf() Write a formatted string to buffer
// sscanf() read data from string buffer
#define găsiac fgetc() //reads the next character from given input stream
#define găsiafgets() //reads n number of characters from file stream
#define luarecaract getchar() //reads next character from stdin
#define luare gets() //reads line from stdin
#define punecaract putchar() //writes a character to stdout
#define pune puts() //writes string to stdout
#define fcitire fread() //reads specified no. of characters from stream
#define fscriere fwrite() //writes specified number of characters to stream
#define fredeschid freopen() //opens a new file with stream associated to another
#define flăut fflush() //flushes any buffered data to the respective device
#define flămurire fseek() //sets file position indicator for given file stream
#define luareacaract getc() //reads next character from input stream
// <ctime>
#define timp time() //Returns current calendar time
#define ceas clock() //returns processor time consumed by program
#define diftimp difftime() //computes difference between two times in seconds
#define asciitimp asctime() //converts calendar time to character representation
#define ctimp ctime() //converts time since epoch to char representation
#define dămitimp gmtime() //converts given time since epoch to UTC time
#define timplocal localtime() //converts given time since epoch to local time
#define șrgftimp strftime() //converts calendar time to multibyte character str
