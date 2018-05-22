package sse.tongji.thunder.model;

import java.util.Date;

public class Terminal {
    private String terminal_description;
    private float peak;
    private int lasting_time;
    private String polarity;
    private Date date;
    private String unit1;
    private String unit2;

    public String getTerminal_description() {
        return terminal_description;
    }

    public void setTerminal_description(String terminal_description) {
        this.terminal_description = terminal_description;
    }

    public float getPeak() {
        return peak;
    }

    public void setPeak(float peak) {
        this.peak = peak;
    }

    public int getLasting_time() {
        return lasting_time;
    }

    public void setLasting_time(int lasting_time) {
        this.lasting_time = lasting_time;
    }

    public String getPolarity() {
        return polarity;
    }

    public void setPolarity(String polarity) {
        this.polarity = polarity;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public String getUnit1() {
        return unit1;
    }

    public void setUnit1(String unit1) {
        this.unit1 = unit1;
    }

    public String getUnit2() {
        return unit2;
    }

    public void setUnit2(String unit2) {
        this.unit2 = unit2;
    }
}