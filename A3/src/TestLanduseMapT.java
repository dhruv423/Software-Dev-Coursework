/**
 * Author: Dhruv Bhavsar
 * Revised: March 16 2020
 * Description: Testing LanduseMapT class
 */

import org.junit.*;
import static org.junit.Assert.*;
import java.util.ArrayList;
import java.util.Arrays;

import src.LuT;
import src.LanduseMapT;
import src.PointT;

public class TestLanduseMapT {

    private LanduseMapT lMap1;
    private LanduseMapT lMap2;
    private LanduseMapT oneRowMap;
    private double eps = 1e-6;



    @Before
    public void setUp() {
        ArrayList<ArrayList<LuT>> l1 = new ArrayList<ArrayList<LuT>>();
        ArrayList<ArrayList<LuT>> l2 = new ArrayList<ArrayList<LuT>>();
        ArrayList<ArrayList<LuT>> oneRow = new ArrayList<ArrayList<LuT>>();

        l1.add(new ArrayList<LuT>(Arrays.asList(LuT.R, LuT.T, LuT.A, LuT.C)));
        l1.add(new ArrayList<LuT>(Arrays.asList(LuT.R, LuT.R, LuT.R, LuT.C)));
        l1.add(new ArrayList<LuT>(Arrays.asList(LuT.T, LuT.A, LuT.A, LuT.R)));
        l1.add(new ArrayList<LuT>(Arrays.asList(LuT.T, LuT.T, LuT.T, LuT.T)));

        l2.add(new ArrayList<LuT>(Arrays.asList(LuT.C, LuT.C, LuT.C, LuT.C)));
        l2.add(new ArrayList<LuT>(Arrays.asList(LuT.R, LuT.R, LuT.R, LuT.R)));
        l2.add(new ArrayList<LuT>(Arrays.asList(LuT.A, LuT.A, LuT.A, LuT.A)));
        l2.add(new ArrayList<LuT>(Arrays.asList(LuT.T, LuT.T, LuT.T, LuT.C)));

        oneRow.add(new ArrayList<LuT>(Arrays.asList(LuT.T, LuT.A)));

        lMap1 = new LanduseMapT(l1, 0.1);
        lMap2 = new LanduseMapT(l2, 989.5);
        oneRowMap = new LanduseMapT(oneRow, 4.0);

    }

    @After
    public void tearDown() {
        lMap1 = null;
        lMap2 = null;
        oneRowMap = null;
    }

    @Test (expected = IllegalArgumentException.class)
    public void testConstructorExceptionEmpty() {
        ArrayList<ArrayList<LuT>> l3 = new ArrayList<ArrayList<LuT>>();
        LanduseMapT l3Map = new LanduseMapT(l3, 45);
    }

    @Test (expected = IllegalArgumentException.class)
    public void testConstructorExceptionScl() {
        ArrayList<ArrayList<LuT>> l3 = new ArrayList<ArrayList<LuT>>();
        l3.add(new ArrayList<LuT>(Arrays.asList(LuT.T, LuT.A)));

        LanduseMapT l3Map = new LanduseMapT(l3, -45);
    }

    @Test (expected = IllegalArgumentException.class)
    public void testConstructorExceptionCols() {
        ArrayList<ArrayList<LuT>> l3 = new ArrayList<ArrayList<LuT>>();
        l3.add(new ArrayList<LuT>(Arrays.asList(LuT.T, LuT.A)));
        l3.add(new ArrayList<LuT>(Arrays.asList(LuT.T)));


        LanduseMapT l3Map = new LanduseMapT(l3, 45);
    }

    @Test (expected = IllegalArgumentException.class)
    public void testConstructorExceptionFirstRowZeroCols() {
        ArrayList<ArrayList<LuT>> l3 = new ArrayList<ArrayList<LuT>>();
        l3.add(new ArrayList<LuT>(Arrays.asList()));
        l3.add(new ArrayList<LuT>(Arrays.asList(LuT.T)));


        LanduseMapT l3Map = new LanduseMapT(l3, 45);
    }

    @Test
    public void testSet1() {
        lMap1.set(new PointT(0,0), LuT.A);
        assertTrue(lMap1.get(new PointT(0,0)) == LuT.A);
    }

    @Test
    public void testSet2() {
        lMap2.set(new PointT(3,3), LuT.R);
        assertTrue(lMap2.get(new PointT(3,3)) == LuT.R);
    }

    @Test
    public void testSet3() {
        oneRowMap.set(new PointT(0,1), LuT.T);
        PointT p1 = new PointT(0,1);
        assertTrue(oneRowMap.get(p1) == LuT.T);
    }

    @Test (expected = IndexOutOfBoundsException.class)
    public void testSetException() {
        lMap1.set(new PointT(0,5), LuT.A);
    }

    @Test
    public void testGet1() {
        assertTrue(lMap1.get(new PointT(2,1)) == LuT.A);
    }

    @Test
    public void testGet2() {
        assertTrue(oneRowMap.get(new PointT(0,1)) == LuT.A);
    }

    @Test
    public void testGet3() {
        assertTrue(lMap2.get(new PointT(3,2)) == LuT.T);
    }

    @Test (expected = IndexOutOfBoundsException.class)
    public void testGetException() {
        lMap1.get(new PointT(5,5));
    }

    @Test
    public void testGetNumRow() {
        assertTrue(lMap2.getNumRow() == 4);
    }

    @Test
    public void testGetNumCol() {
        assertTrue(lMap1.getNumCol() == 4);
    }

    @Test
    public void testGetNumScale() {
        assertTrue(oneRowMap.getScale() == 4.0);
    }

    @Test
    public void testCount1() {
        assertTrue(oneRowMap.count(LuT.C) == 0);
    }

    @Test
    public void testCount2() {
        assertTrue(lMap2.count(LuT.R) == 4);
    }

    @Test
    public void testCount3() {
        assertTrue(lMap1.count(LuT.A) == 3);
    }

    @Test
    public void testCountRow1() {
        assertTrue(lMap2.countRow(LuT.R, 0) == 0);
    }

    @Test
    public void testCountRow2() {
        assertTrue(lMap1.countRow(LuT.R, 1) == 3);
    }

    @Test
    public void testCountRow3() {
        assertTrue(oneRowMap.countRow(LuT.C, 0) == 0);
    }

    @Test (expected = IndexOutOfBoundsException.class)
    public void testCountRowException() {
        lMap2.countRow(LuT.R, -1);
    }

    @Test
    public void testArea1() {
        assertEquals(lMap2.area(LuT.R), 3916441, eps);
    }

    @Test
    public void testArea2() {
        assertEquals(oneRowMap.area(LuT.C), 0, eps);
    }

    @Test
    public void testArea3() {
        assertEquals(lMap1.area(LuT.T), 0.06, eps);
    }

}