package org.salyrus.cvtesting;

import static org.junit.Assert.assertTrue;

import org.junit.Before;
import org.junit.Test;

public class AppTest {

    private App app;

    @Before
    public void setUp() {
        app = new App();
    }

    @Test
    public void shouldAnswerWithTrue() {
        app.runSimpleScenario();
        assertTrue( true );
    }
}
