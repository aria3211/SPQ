#include <iostream>




using namespace std;

const int N = 3;             
const int EMPTY = 0;       
const int STOP_INPUT = -1;  

void input_sud(int sud[][N*N]);
bool fill_sud(int sud[][N*N], int row, int col);
void print_sud(const int sud[][N*N]);
bool is_legal(const int sud[][N*N], int row, int col, int val);
bool is_row_ok(const int row[], int col, int val);
bool is_col_ok(const int sud[][N*N], int row, int col, int val);
bool is_sqr_ok(const int sud[][N*N], int row, int col, int val);



int main()
{
    int sud[N*N][N*N] = { { EMPTY } };  

    input_sud(sud);
    fill_sud(sud, 0, 0);
    print_sud(sud);

    return 0;
}


void input_sud(int sud[][N*N])
{
    for(int i = 0; i < N*N; i++)
        for(int j = 0; j < N*N; j++)
            cin >> sud[i][j];
}

//======== Fill Sudoku =========//
// Tries to fill-in the given sudoku board
// according to the sudoku rules.
// Returns whether it was possible to solve it or not.
bool fill_sud(int sud[][N*N], int row, int col)
{

    int next_row = (col == N*N - 1) ? row + 1 : row;

  
    int next_col = (col + 1) % (N*N);

    
    if(row == N*N)
        return true;

    
    if(sud[row][col] != EMPTY)
        return fill_sud(sud, next_row, next_col);

    
    for(int value = 1; value <= N*N; value++)
    {
        sud[row][col] = value;

        if(is_legal(sud, row, col, value) && fill_sud(sud, next_row, next_col))
            return true;

        sud[row][col] = EMPTY;
    }

  
    return false;
}


void print_sud(const int sud[][N*N])
{
    for(int i = 0; i < N*N; i++)
    {
        for(int j = 0; j < N*N; j++)
            cout << sud[i][j] << ' ';
        cout << endl;
    }
}


bool is_legal(const int sud[][N*N], int row, int col, int val)
{
    return (is_row_ok(sud[row], col, val) &&
            is_col_ok(sud, row, col, val) &&
            is_sqr_ok(sud, row, col, val));
}

//========= Is Row OK =========//
// Checks and returns whether it's legal
// to put 'val' in A specific row.
bool is_row_ok(const int row[], int col, int val)
{
    for(int i = 0; i < N*N; i++)
        if(i != col && row[i] == val)
            return false;       

    return true;
}

//========= Is Column OK =========//
// Checks and returns whether it's legal
// to put 'val' in A specific column.
bool is_col_ok(const int sud[][N*N], int row, int col, int val)
{
    for(int i = 0; i < N*N; i++)
        if(i != row && sud[i][col] == val)
            return false;       

    return true;
}

//========= Is Square OK =========//
// Checks and returns whether it's legal
// to put 'val' in A specific square.
bool is_sqr_ok(const int sud[][N*N], int row, int col, int val)
{
    int row_corner = (row / N) * N;
    

    int col_corner = (col / N) * N;
    

    for(int i = row_corner; i < (row_corner + N); i++)
        for(int j = col_corner; j < (col_corner + N); j++)
            if((i != row || j != col) && sud[i][j] == val)
                return false;       // Found the same value again!

    return true;
}
