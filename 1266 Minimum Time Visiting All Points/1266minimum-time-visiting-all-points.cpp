class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int sec=0,x,y;
        for(int i=1;i<points.size();i++){
            x=abs(points[i][0]-points[i-1][0]);
            y=abs(points[i][1]-points[i-1][1]);
            sec+=(x>y)?x:y;
        }
        return sec;
    }
};