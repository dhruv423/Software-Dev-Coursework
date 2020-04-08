/**
 * Author: Dhruv Bhavsar
 * Revised: March 16 2020
 * Description: DemT ADT class
 */

package src;
import java.util.ArrayList;

/**
 * @brief An ADT that represents the grid (Seq2D) with type Integer
 */
public class DemT extends Seq2D<Integer> {

    /**
     * @brief Constructor that creates a new DemT object
     * @details Same exceptions as Seq2D apply here, using super to call the parent constructor
     * @param S The ArrayList in a Arraylist of type Integer
     * @param scl type double, scale - length of each side of each cell in the grid
     */
    public DemT(ArrayList<ArrayList<Integer>> S, double scl) {
        super(S, scl);
    }

    /**
     * @brief Method that calculate the total of all the values in all of the cells
     * @details Loop over the number of rows and number of columns, make a new pointT and use the get method to find
     * value
     * @return Integer - total of all cells' values
     */
    public Integer total() {
        Integer total = 0;

        for (int i = 0; i < getNumRow(); i ++) {
            for (int j = 0; j < getNumCol(); j++) {
                total += get(new PointT(i, j));
            }
        }
        return total;
    }

    /**
     * @brief Method that finds the maximum value in the 2d grid of integers
     * @details Loop over the number of rows and number of columns, make a new pointT and use the get method to find
     * value and compare it with the current max
     * @return Integer - maximum value in the grid
     */
    public Integer max() {
        Integer max = Integer.MIN_VALUE;

        for (int i = 0; i < getNumRow(); i ++) {
            for (int j = 0; j < getNumCol(); j++) {
                Integer val = get(new PointT(i, j));
                max = Math.max(max, val);
            }
        }
        return max;
    }

    /**
     * @brief Method to find out if the total in each row is increasing as the row number increases
     * @details If num of rows is 1, then its not ascending.
     * @return True if the rows are ascending else false
     */
    public boolean ascendingRows() {
        if (getNumRow() == 1) {
            return false;
        }

        for (int i = 1; i < getNumRow(); i++) {
            if (rowSum(i) < rowSum(i - 1)) {
                return false;
            }
        }
        return true;
    }

    private Integer rowSum(int rowNum) {
        Integer sum = 0;
        for (int j = 0; j < getNumCol(); j++) {
            sum += get(new PointT(rowNum, j));
        }
        return sum;
    }
}