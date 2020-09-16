package a9ÔÂ16ºÅ;

public class cc {
static int[] getArr(int[] arr) {
	for(int i1=0; i1<arr.length-1; i1++) {
		for(int j=0;j<arr.length-1-i1;j++) {
			if(arr[j]<arr[j+1]) {
				int te=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=te;
					}
			}	
	}
	return arr;
}
}