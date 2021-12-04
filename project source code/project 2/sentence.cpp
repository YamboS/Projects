
#include <iostream>
#include <string>
#include "sentence.h"

using namespace std;


/******************************************************************************************************************************************************
Name:default constructor
Pre-Condition:The front, back and count are uninitialized
Post-Condition:The front, back and count are initialized
Description: The front, back, and count are set to zero
******************************************************************************************************************************************************/
sentence::sentence()
{

	front = 0;
	back = 0;
	count = 0;
}

/******************************************************************************************************************************************************
Name:Explicit constructor
//Pre-Condition: The node has not been created or the initalized sentence
Post-Condition:The node has been created and the sentence has been initialized
Description:This function takes all the words and spaces in the string and make them into nodes
******************************************************************************************************************************************************/
sentence::sentence(const string& s)
{

	front = 0;
	back = 0;
	count = 0;
	string temp; //parse
	string space = " ";
	if (s.length() != 0)
	{
		for (int i = 0; i < (int)s.length(); i++)
		{
			if (s[i] != ' ')
			{
				temp += s[i];
			}
			if (s[i] == ' ')
			{
				add_back(temp);
				add_back(space);
				temp = "";
			}
			if (s[i + 1]=='\0') {
				add_back(temp);
				temp = "";


			}

		}
		add_back(temp);
	}
}

/******************************************************************************************************************************************************
Name:copy constructor
Pre-Condition: The linked list has not been copied to the other object
Post-Condition:The linked list has been copied to the other object
Description:This function copies the nodes from one of the linked list to the other object
******************************************************************************************************************************************************/
sentence::sentence(const sentence& org) {
	front = 0;
	back = 0;
	count = 0;
	word* p = org.front;

	while (p != 0) {

		add_back(p->term);
		p = p->next;

	}
}

/******************************************************************************************************************************************************
Name:Destructor
Pre-Condition:The memory allocated by the new node has not been deleted
Post-Condition:The memory allocated by the new node has been deleted
Description: This function uses delete to reallocate memory allocated by new for the node
******************************************************************************************************************************************************/
sentence::~sentence()
{
	cout << "Destructor has been called\n";
	while (front != 0)
	{
		word* p = front;
		front = front->next;
		delete p;
	}

}//Destructor: The destructor will de-allocate all memory allocated for the word. Put the message



/******************************************************************************************************************************************************
Name:Length
Pre-Condition:The length of all the strings in the node have not been determined
Post-Condition:The length of all the strings in the nodes have been added together
Description:parses the linked list and adds together the length of the strings in  the linked list
******************************************************************************************************************************************************/
int sentence::length()
{
	int length = 0;
	word* chosen = this->front;
	if (chosen == 0)
	{
		return length;
	}
	else
	{
		while (chosen != 0)
		{
			length += chosen->term.length();
			chosen = chosen->next;
		}
		return length;
	}

}

/******************************************************************************************************************************************************
Name: add back
Pre-Condition: No new node is added to the linked list
Post-Condition:A new node is added to the back of the list
Description:This function adds to the end of the link list to whatever function it is called by
******************************************************************************************************************************************************/
void sentence::add_back(const string& s)
{

	if (isEmpty())
	{
		front = new word;
		front->term = s;
		front->next = 0;
		back = front;
		count++;
	}
	else
	{
		word* p = new word;
		word* b = front;
		while (b->next != 0) {
		
			b = b->next;
}
		b->next = p;
		p->next = 0;
		p->term = s;
		back->next = p;
		back = p;
		count++;
	
	
	
	
	
	
	
	}
	count++;
}

/******************************************************************************************************************************************************
Name:operator<<
Pre-Condition:This operator is not overloaded for member values
Post-Condition:This operator is overloaded for member values
Description:The function overloads the extraction operator so the it can be used in cout
******************************************************************************************************************************************************/
ostream& operator<<(ostream& out, const sentence& org)
{
	word* p = org.front;
	while (p != 0)
	{
		out << p->term;
		p = p->next;
	}
	return out;
}

/******************************************************************************************************************************************************
Name:operator =
Pre-Condition: The string being passed through the argument is not added to the linked list
Post-Condition:The string being passed through the argument is added to the linked list
Description: Takes the string like the explict value constructor and adds to the end of a linked list with the add_back function
******************************************************************************************************************************************************/
void sentence::operator=(const string& s)
{
	front = 0;
	back = 0;
	count = 0;
	string temp; //parse
	string space = " ";
	if (s.length() != 0)
	{
		for (int i = 0; i < (int)s.length(); i++)
		{
			if (s[i] != ' ')
			{
				temp += s[i];
			}
			if (s[i] == ' ')
			{
				add_back(temp);
				add_back(space);
				temp = "";
			}
			if (s[i + 1] == '\0') {
				add_back(temp);
				temp = "";


			}

		}
		add_back(temp);
	}
}


/******************************************************************************************************************************************************
Name:operator+
Pre-Condition:The content of the second linked list have not been added to the end of the first linked list
Post-Condition:The content of the second linked list have been added to the end of the first linked list
Description:Uses the add back to basically add the linked list of one object to the end of another one
******************************************************************************************************************************************************/
void sentence::operator+(sentence& b)
{
	word* p = b.front;
	if (p != 0)
	{
		while (p != 0)
		{
			add_back(p->term);
			p = p->next;
		}
	}
	else
	{
		return;
	}
}

/******************************************************************************************************************************************************
Name:Is Equal
Pre-Condition:The string has not been checked to see if there are matching strings in a different linked list
Post-Condition:The string has either been found in the list or has not been and false is returned
Description: Directly compares the strings in two different list
******************************************************************************************************************************************************/

bool sentence::isEqual(sentence& B)
{
	word* p = this->front;
	word* ptr = B.front;
	if (this->count != B.count)
	{

		return false;
	}
	else
	{
		while (p != 0)
		{
			if (p->term != ptr->term)
			{
				return false;
			}
			p = p->next;
			ptr = ptr->next;
		}
		return true;
	}
}

/******************************************************************************************************************************************************
Name:Remove
Pre-Condition:Whatever string that is being searched for has not yet been looked for or removed
Post-Condition Whatever string that is being searched for deletion has been looked for and possibly removed
Description:This calls the search function to see if the looked for string is in the linked list and if it is it returns to the main function
the string is the deleted from the linked list
******************************************************************************************************************************************************/
void sentence::remove(const string& subject)
{
	word* p = Search(subject);

	if (p == 0)
	{

	}
	else
	{
		if (p == front && front == back)
		{
			delete p;
			count--;
			front = back = 0;
		}
		else if (p == front)
		{
			front = front->next;
			delete p;
			count--;
		}
		else
		{
			word* Bptr = front;

			while (Bptr != 0 && Bptr->next!=p)
			{
				Bptr = Bptr->next;
			}
			if (p == back)
			{
				back = Bptr;
			}
			Bptr->next = p->next;
			delete p;
			count--;
		}
	}
}
/******************************************************************************************************************************************************
Name:Search
Pre-Condition:the string has not been searched for in the linked list
Post-Condition the string has been searched for in the linked list and the address was either returned or the current object
Description:This function searches  for the string in  the linked list
******************************************************************************************************************************************************/
word* sentence::Search(const string& subject)
{

	word* p = front;

	while (p != 0)
	{
		if (p->term == subject)
		{
			return p;
		}
		p = p->next;
	}
	return p;

}
/******************************************************************************************************************************************************
Name:Operator=
Pre-Condition:the assignment operator has not been overloaded with chaining yet
Post-Condition the assignment operator has been overloaded with chaining to take a word
Description:This function is very similar to the copy constructor and uses the addback function
******************************************************************************************************************************************************/
sentence& sentence::operator=(const sentence& w){
	front = 0;
	back = 0;
	count = 0;
	word* p = w.front;

	while (p != 0) {

		add_back(p->term);

		p = p->next;

	}

	return *this;
}

