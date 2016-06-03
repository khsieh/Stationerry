package com.saito.logerrors;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        button = (Button)findViewById(R.id.button);
    }

    public void throwException(View v){
        Toast.makeText(this, "Throwing Null Exception", Toast.LENGTH_SHORT).show();
        throw new IndexOutOfBoundsException("Throwing out of bounds exception!");

    }
}
