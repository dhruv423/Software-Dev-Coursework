/**
 * Author: Dhruv Bhavsar
 * Revised: March 16 2020
 * Description: Testing PointT class
 */

import org.junit.*;
import static org.junit.Assert.*;
import src.PointT;

public class TestPointT {

    private PointT p1;
    private PointT p2;
    private PointT p3;
    private PointT p4;

    @Before
    public void setUp()
    {
        p1 = new PointT(0, 0);
        p2 = new PointT(34, 56);
        p3 = new PointT(-4, -7);
        p4 = new PointT(3,-2);
    }

    @After
    public void tearDown()
    {
        p1 = null;
        p2 = null;
        p3 = null;
        p4 = null;
    }

    @Test
    public void testRow1() {
        assertTrue(p1.row() == 0);
    }

    @Test
    public void testRow2() {
        assertTrue(p2.row() == 34);
    }

    @Test
    public void testRow3() {
        assertTrue(p3.row() == -4);
    }

    @Test
    public void testRow4() {
        assertTrue(p4.row() == 3);
    }

    @Test
    public void testCol1() {
        assertTrue(p1.col() == 0);
    }

    @Test
    public void testCol2() {
        assertTrue(p2.col() == 56);
    }

    @Test
    public void testCol3() {
        assertTrue(p3.col() == -7);
    }

    @Test
    public void testCol4() {
        assertTrue(p4.col() == -2);
    }

    @Test
    public void testTranslate1() {
        PointT p5 = p1.translate(p2.row(), p2.col());
        assertTrue(p5.row() == p2.row() && p5.col() == p2.col());
    }

    @Test
    public void testTranslate2() {
        PointT p5 = p2.translate(p2.row(), p2.col());
        assertTrue(p5.row() == 68 && p5.col() == 112);
    }

    @Test
    public void testTranslate3() {
        PointT p5 = p3.translate(p1.row(), p1.col());
        assertTrue(p5.row() == p3.row() && p5.col() == p3.col());
    }

    @Test
    public void testTranslate4() {
        PointT p5 = p4.translate(45, -87);
        assertTrue(p5.row() == 48 && p5.col() == -89);
    }

}