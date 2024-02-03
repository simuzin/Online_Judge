#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int arr[1000000] = { 0 };

int main()
{
	int N;

	cin >> N;
	
	arr[0] = 0;
	arr[1] = 0;
	arr[2] = 1;
	arr[3] = 1;
	int count = 0 ;
	int num;

	int small_num;
	for(int i=4 ; i<= N; i ++)
	{
		num = i;
		while (num > 1)
		{
			if (num % 3 == 0)
			{
				if (num % 2 == 0)
				{
					arr[num] = min(arr[num / 3] + 1, arr[num / 2] + 1);
				}
				else
				{
					arr[num] = min(arr[num / 3] + 1,arr[num-1]+1);
				}

				if (arr[num] == arr[num / 3] + 1)
				{
					num = num / 3;
				}
				else if (arr[num] == arr[num - 1] + 1)
				{
					num--;
				}
				else
				{
					num= num/2;
				}
			}
			else if (num % 2 == 0)
			{
				arr[num] = min(arr[num-1]+1,arr[num / 2] + 1);
				if (arr[num] == arr[num / 2] + 1)
				{
					num = num / 2;
				}
				else
				{
					num--;
				}
			}
			else
			{
				arr[num] = arr[num - 1] + 1;
				num--;

			//cout << num << endl;
			}		}
		//cout << i << " : " << arr[i] << endl;
	//	cout << "---------- " << endl;
	}		

	cout << arr[N];
	return 0;
}