/**
 * Author: Dhruv Bhavsar
 * Revised: March 16 2020
 * Description: LanduseMapT ADT class
 */

package src;
import java.util.ArrayList;

/**
 * @brief An ADT that represents Landuse types on the grid (Seq2D)
 *
 */
public class LanduseMapT extends Seq2D<LuT> {

    /**
     * @brief Constructor that creates a new LanduseMapT
     * @details Same exceptions as Seq2D apply here, using super to call the parent constructor
     * @param S The ArrayList in a Arraylist of type LuT
     * @param scl type double, scale - length of each side of each cell in the grid
     */
    public LanduseMapT(ArrayList<ArrayList<LuT>> S, double scl) {
        super(S, scl);
    }

}