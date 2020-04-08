/**
 * Author: Dhruv Bhavsar
 * Revised: March 16 2020
 * Description: PointT ADT class
 */

package src;

/**
 * @brief An ADT that represents a point
 */
public class PointT {

    // Row variable
    private int r;
    // Column variable
    private int c;

    /**
     * @brief Constructor to create a PointT object
     * @param row Takes the row number as an int
     * @param col Takes the col number as an int
     */
    public PointT(int row, int col) {
        this.r = row;
        this.c = col;
    }

    /**
     * @brief Getter for row variable
     * @return row variable (int)
     */
    public int row() {
        return this.r;
    }

    /**
     * @brief Getter for column variable
     * @return column variable (int)
     */
    public int col() {
        return this.c;
    }

    /**
     * @brief Method to translate the current point by given row and column parameters
     * @param dr Change in row position (int)
     * @param dc Change in column position (int)
     * @return New PointT with the new coordinates after translate
     */
    public PointT translate(int dr, int dc) {
        return new PointT(r + dr, c + dc);
    }





}