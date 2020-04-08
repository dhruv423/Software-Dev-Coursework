/**
 * Author: Dhruv Bhavsar
 * Revised: March 16 2020
 * Description: Testing DemT class
 * Note: I didn't test exceptions in this since they were the same exceptions tested in TestLanduseMapT
 */

import org.junit.*;
import static org.junit.Assert.*;
import java.util.ArrayList;
import java.util.Arrays;

import src.PointT;
import src.DemT;

public class TestDemT {

    private DemT dMap1;
    private DemT dMap2;
    private DemT oneRowMap;
    private double eps = 1e-6;



    @Before
    public void setUp() {
        ArrayList<ArrayList<Integer>> d1 = new ArrayList<ArrayList<Integer>>();
        ArrayList<ArrayList<Integer>> d2 = new ArrayList<ArrayList<Integer>>();
        ArrayList<ArrayList<Integer>> oneRow = new ArrayList<ArrayList<Integer>>();

        d1.add(new ArrayList<Integer>(Arrays.asList(23, 55, 45, 43)));
        d1.add(new ArrayList<Integer>(Arrays.asList(44, 56, 36, 31)));
        d1.add(new ArrayList<Integer>(Arrays.asList(45, 12, 4, 200)));
        d1.add(new ArrayList<Integer>(Arrays.asList(100, 56, 58, 100)));

        d2.add(new ArrayList<Integer>(Arrays.asList(-1, -3, -4, -90)));
        d2.add(new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4)));
        d2.add(new ArrayList<Integer>(Arrays.asList(11, 3, -7, -20)));
        d2.add(new ArrayList<Integer>(Arrays.asList(20, 20, 20, 20)));

        oneRow.add(new ArrayList<Integer>(Arrays.asList(45, -45)));

        dMap1 = new DemT(d1, 5.5);
        dMap2 = new DemT(d2, 1.4);
        oneRowMap = new DemT(oneRow, 85.0);

    }

    @After
    public void tearDown() {
        dMap1 = null;
        dMap2 = null;
        oneRowMap = null;
    }

    @Test
    public void testSet1() {
        dMap1.set(new PointT(3, 1), 45);
        assertTrue(dMap1.get(new PointT(3, 1)) == 45);
    }

    @Test
    public void testSet2() {
        dMap2.set(new PointT(0, 3), -567);
        assertTrue(dMap2.get(new PointT(0, 3)) == -567);
    }

    @Test
    public void testSet3() {
        oneRowMap.set(new PointT(0, 0), 4534);
        assertTrue(oneRowMap.get(new PointT(0, 0)) == 4534);
    }

    @Test
    public void testGet1() {
        assertTrue(dMap1.get(new PointT(0, 3)) == 43);
    }

    @Test
    public void testGet2() {
        assertTrue(dMap2.get(new PointT(3, 0)) == 20);
    }

    @Test
    public void testGet3() {
        assertTrue(oneRowMap.get(new PointT(0, 0)) == 45);
    }

    @Test
    public void testGetNumRow() {
        assertTrue(dMap1.getNumRow() == 4);
    }

    @Test
    public void testGetNumCol() {
        assertTrue(dMap2.getNumCol() == 4);
    }

    @Test
    public void testGetScale() {
        assertTrue(dMap1.getScale() == 5.5);
    }

    @Test
    public void testCount1() {
        assertTrue(dMap1.count(100) == 2);
    }

    @Test
    public void testCount2() {
        assertTrue(dMap2.count(20) == 4);
    }

    @Test
    public void testCount3() {
        assertTrue(oneRowMap.count(0) == 0);
    }

    @Test
    public void testCountRow() {
        assertTrue(dMap2.countRow(20, 3) == 4);
    }

    @Test
    public void testArea1() {
        assertEquals(dMap2.area(-20), 1.96, eps);
    }

    @Test
    public void testArea2() {
        assertEquals(dMap1.area(100), 60.5, eps);
    }

    @Test
    public void testTotal1() {
        assertTrue(dMap1.total() == 908);
    }

    @Test
    public void testTotal2() {
        assertTrue(oneRowMap.total() == 0);
    }

    @Test
    public void testMax1() {
        assertTrue(dMap1.max() == 200);
    }

    @Test
    public void testMax2() {
        assertTrue(oneRowMap.max() == 45);
    }

    @Test
    public void testMax3() {
        assertTrue(dMap2.max() == 20);
    }

    @Test
    public void testAscendingRows1() {
        assertFalse(oneRowMap.ascendingRows());
    }

    @Test
    public void testAscendingRows2() {
        assertTrue(dMap1.ascendingRows());
    }

    @Test
    public void testAscendingRows3() {
        assertFalse(dMap2.ascendingRows());
    }

}
