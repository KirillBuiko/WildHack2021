#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdio.h>
#include <string>
#include "DeblurFilter.hpp"


using namespace cv;
using namespace std;

int main(int argc, char* argv[])
{
	int sigma1 = 2;
	int snr = 26;
	//string strInFileName = "In\\2222.tif";
	char Buf[5] = { '\0' };
	for (int i = 0; i < 1; i++)
	{
		Mat imgIn;
		_itoa_s(i, Buf, 10);
		imgIn = imread(string("In\\img_" + string(Buf) + ".jpg"), IMREAD_UNCHANGED);
		//imgIn = imread(strInFileName, IMREAD_UNCHANGED);
		//cout << string("img_" + string(Buf) + ".tif") << endl;
		if (imgIn.empty()) //check whether the image is loaded or not
		{
			cout << "ERROR : Image cannot be loaded..!!" << endl;
			//system("pause"); //wait for a key press
			continue;
		}
		Mat imgOut;
		DeblurFilter filter;
		double t0, t1;
		t0 = (double)getTickCount();
		filter.Process(imgIn, imgOut, sigma1, snr);
		t1 = ((double)getTickCount() - t0) / getTickFrequency();
		cout << "Total elapsed  CPU time (ms)= " << 1000 * t1 << endl;
		cout << endl;

		imgOut.convertTo(imgOut, CV_8U);
		normalize(imgOut, imgOut, 0, 255, NORM_MINMAX);

		string strOutFileName = "Out\\img_";
		strOutFileName += string(Buf) + ".jpg";
		

		imwrite(strOutFileName, imgOut);
	}
	return 0;
}