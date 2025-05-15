bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    for(int i=0;i<matrixSize;i++){
        for(int j=0;j<*matrixColSize;j++){
            if(target==*(*(matrix+i)+j)){
                return true;
            }
        }
    }
    return false;
}