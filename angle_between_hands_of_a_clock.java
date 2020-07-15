class Solution {
    public double angleClock(int hour, int minutes) {
        if (hour == 12) hour = 0;
        double hhAngle = (360/12 * hour) + (360/12 * (double)minutes/60);
        double mmAngle = (double)360/60 * minutes;

        if (hhAngle > mmAngle) {
            double diff = hhAngle - mmAngle;
            return diff <= 180 ? diff : 360 - diff;
        } else {
            double diff = mmAngle - hhAngle;
            return diff <= 180 ? diff : 360 - diff;
        }
    }
}