#include <iostream>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    string board[50];
    for (int i = 0; i < n; i++) {
        cin >> board[i];
    }
    
    int count, min = 64;
    for (int i = 0; i < n - 7; i++) {
        for (int j = 0; j < m - 7; j++) {
            for (int c = 0; c < 2; c++) {
                count = 0;
                for (int x = i; x < i + 8; x++) {
                    for (int y = j; y < j + 8; y++) {
                        if (c == 0) {
                            if (x % 2 == 0 && y % 2 == 0)
                                if (board[x][y] != 'W')
                                    count++;
                            if (x % 2 == 0 && y % 2 == 1)
                                if (board[x][y] != 'B')
                                    count++;
                            if (x % 2 == 1 && y % 2 == 0)
                                if (board[x][y] != 'B')
                                    count++;
                            if (x % 2 == 1 && y % 2 == 1)
                                if (board[x][y] != 'W')
                                    count++;
                        }
                        else {
                            if (x % 2 == 0 && y % 2 == 0)
                                if (board[x][y] != 'B')
                                    count++;
                            if (x % 2 == 0 && y % 2 == 1)
                                if (board[x][y] != 'W')
                                    count++;
                            if (x % 2 == 1 && y % 2 == 0)
                                if (board[x][y] != 'W')
                                    count++;
                            if (x % 2 == 1 && y % 2 == 1)
                                if (board[x][y] != 'B')
                                    count++;
                        }
                    }
                }
                if (count < min)
                    min = count;
            }
        }
    }

    cout << min << endl;
    
    return 0;
}