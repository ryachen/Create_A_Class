import java.util.Random;
public class Sudoku_Board {
	
	

	public static void main(String[] args) {
		
		int[][] sudoku_board = new int[10][10];

		createboard(sudoku_board);
		
		startingnumbers(sudoku_board);
	for (int j = 0; j < 9; ++j) {
		for (int i = 0; i < 9; ++i) {
		
			System.out.print(sudoku_board[j][i]);
		
			
		}System.out.println();
		
		
	}
		
		
		

	}
	public static int[][] createboard(int [][] board ){
		
		
		
			for (int i = 0; i < 9; ++i) {
			
				for (int j = 0; j < 9; ++j) {
				board [i][j] = 0;
				
				
				
			}
			
		}
		
		
		return board;
		
	}
	public static int[][] startingnumbers(int [][] board ){
		
		
		for (int i = 0; i < 100; ++i) {
		
		Random rand = new Random();
		int firstindex = rand.nextInt(9);
		Random rand2 = new Random();
		int secondindex = rand2.nextInt(9);
		Random rand3 = new Random();
		int value = rand3.nextInt(9);
		
		if (board [firstindex][secondindex] == 0) {
			
			for (int x = 0; x < 9; ++x) {
				if (board[firstindex][x] == value && x != secondindex && value != 0) {
					System.out.println(value);
					value = 0;
					break;
				}
				if (board[x][secondindex] == value && x != firstindex && value != 0) {
					value = 0;
					break;
				}
			}
			for (int a = 0; a < 3; ++a) {
				for (int b = 0; b < 3; ++b) {
					if (board[a][b] == value && value != 0) {
						value = 0;
						break;
						
					}
				}
			}
			for (int a = 3; a < 6; ++a) {
				for (int b = 0; b < 3; ++b) {
					if (board[a][b] == value && value != 0) {
						value = 0;
						break;
						
					}
				}
			}
			for (int a = 6; a < 9; ++a) {
				for (int b = 0; b < 3; ++b) {
					if (board[a][b] == value && value != 0) {
						value = 0;
						break;
						
					}
				}
			}
			for (int a = 0; a < 3; ++a) {
				for (int b = 3; b < 6; ++b) {
					if (board[a][b] == value && value != 0) {
						value = 0;
						break;
						
					}
				}
			}
			for (int a = 3; a < 6; ++a) {
				for (int b = 3; b < 6; ++b) {
					if (board[a][b] == value && value != 0) {
						value = 0;
						break;
						
					}
				}
			}
			for (int a = 6; a < 9; ++a) {
				for (int b = 3; b < 6; ++b) {
					if (board[a][b] == value && value != 0) {
						value = 0;
						break;
						
					}
				}
			}
			for (int a = 0; a < 3; ++a) {
				for (int b = 6; b < 9; ++b) {
					if (board[a][b] == value && value != 0) {
						value = 0;
						break;
						
					}
				}
			}
			for (int a = 3; a < 6; ++a) {
				for (int b = 6; b < 9; ++b) {
					if (board[a][b] == value && value != 0) {
						value = 0;
						break;
						
					}
				}
			}
			for (int a = 6; a < 9; ++a) {
				for (int b = 6; b < 9; ++b) {
					if (board[a][b] == value && value != 0) {
						value = 0;
						break;
						
					}
				}
			}
			
			
			board [firstindex][secondindex] = value;
			
		}
		
		}
		return board;
	
		
	}
	
	
}



