/**
 * Author: Dhruv Bhavsar
 * Revised: March 16 2020
 * Description: Seq2D ADT class
 */
package src;

import java.util.ArrayList;

/**
 * @brief An ADT that represents a matrix
 * @param <T> Type T for generality
 */
public class Seq2D<T> {

    private ArrayList<ArrayList<T>> s;
    private double scale;
    private int nRow;
    private int nCol;

    /**
     * @brief Constructor to create a new Seq2D, number of columns must be the same for each row
     * @param S Arraylist of Arraylist, cannot be empty else exception is thrown
     * @param scl Scale, cannot be less than 0 else exception is thrown
     * @throws IllegalArgumentException for scl being a negative, empty sequence, number of columns inconsistent
     */
    public Seq2D(ArrayList<ArrayList<T>> S, double scl) {
        if (scl <= 0) {
            throw new IllegalArgumentException("Scale cannot be negative");
        }

        if (S.size() == 0) {
            throw new IllegalArgumentException("Sequence is empty");
        }

        if(S.get(0).size() == 0) {
            throw new IllegalArgumentException("Number of columns in the first row is 0");
        }

        for (int i = 1; i < S.size(); i++) {
            if (S.get(i).size() != S.get(0).size()) {
                throw new IllegalArgumentException("Number of columns not the same in each row");
            }
        }

        this.s = S;
        this.scale = scl;
        this.nCol = S.get(0).size();
        this.nRow = S.size();

    }

    /**
     * @brief Method to set a specific element in the sequence to a value given by the parameter,
     * @details if point doesn't exist in the sequence exception thrown IndexOutofBounds
     * @param p PointT, the specific element in the sequence
     * @param v Type T, Set the element to
     * @throws IndexOutOfBoundsException if not valid point
     */
    public void set(PointT p, T v) {
        if (!validPoint(p.row(), p.col())) {
            throw new IndexOutOfBoundsException("Point doesn't lie in the map");
        }
        s.get(p.row()).set(p.col(), v);
    }

    /**
     * @brief Method to get the value at the specified index by a PointT
     * @param p PointT, the specific index
     * @return value of whats in the index Type T
     * @throws IndexOutOfBoundsException if not valid point
     */
    public T get(PointT p) {
        if (!validPoint(p.row(), p.col())) {
            throw new IndexOutOfBoundsException("Point doesn't lie in the map");
        }
        return s.get(p.row()).get(p.col());
    }

    /**
     * @brief Getter to get the number of rows in the sequence
     * @return int value of rows
     */
    public int getNumRow() {
        return this.nRow;
    }

    /**
     * @brief Getter to get the number of columns in the sequence
     * @return int value of columns
     */
    public int getNumCol() {
        return this.nCol;
    }

    /**
     * @brief Getter to get the scale
     * @return double value of scale
     */
    public double getScale() {
        return this.scale;
    }

    /**
     * @brief Method to find out how many times a value exists in the sequence
     * @details Loop over each row and call the countRow method to find the total count in that row
     * @param t Type T, the value to find in the sequence
     * @return count Type int indicating how many times it appeared
     */
    public int count(T t) {
        int count = 0;
        for (int i = 0; i < nRow; i ++){
            count += countRow(t, i);
        }
        return count;
    }

    /**
     * @brief Method to count how many times the value t appears in row i
     * @details Check if the inputed row number is valid, loop over all the elements in the ith arraylist
     * @param t Type T, value to check
     * @param i int row number
     * @throws IndexOutOfBoundsException if not a valid row
     * @return count - number of occurences
     */
    public int countRow(T t, int i) {
        if (!validRow(i)) {
            throw new IndexOutOfBoundsException("Index is not a valid row");
        }
        int count = 0;
        for (int j = 0; j < nCol; j++) {
            if (s.get(i).get(j).equals(t)) {
                count++;
            }
        }
        return count;
    }

    /**
     * @brief Method to calculate the total area in the grid taken up by cell value t
     * @details The length of each side of each cell is the scale hence the scale squared
     * @param t cell value to look for, type T
     * @return area type double
     */
    public double area(T t) {
        return count(t) * Math.pow(this.scale, 2);
    }

    private boolean validRow(int i) {
        return (0 <= i && i <= nRow - 1);
    }

    private boolean validCol(int j) {
        return (0 <= j && j <= nCol - 1);
    }

    private boolean validPoint(int i, int j) {
        return validRow(i) && validCol(j);
    }
}