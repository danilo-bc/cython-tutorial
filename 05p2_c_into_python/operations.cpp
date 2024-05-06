#include <vector>
#include <numeric>
#include <iostream>

using namespace std;

double cpp_convolve(const vector<vector<double> >& in_a_v, const vector<vector<double> >& in_b_v, int n_vecs) {
    double acc_out = 0;
    for (int n = 0; n < n_vecs; n++){
        vector<double> in_a(in_a_v[n]);
        vector<double> in_b(in_b_v[n]);

        int in_a_size = in_a.size();
        int in_b_size = in_b.size();
        int output_size = in_a_size + in_b_size - 1;
        vector<double> output(output_size, 0);
        
        for (int i = 0; i < output_size; i++) {
            for (int j = 0; j < in_b_size; j++) {
                if (i - j >= 0 && i - j < in_a_size) {
                    output[i] += in_a[i - j] * in_b[j];
                }
            }
        }
        int half_output_size = output_size / 2;
        vector<double> even_odd_subtraction(half_output_size, 0.0);
        double partial_acc = 0;
        for (int i = 1; i <= half_output_size; i++){
            even_odd_subtraction[i - 1] = output[2*i] - output[2*i-1];
            partial_acc += even_odd_subtraction[i - 1];
        }
        acc_out = acc_out + accumulate(even_odd_subtraction.begin(), even_odd_subtraction.end(), 0.0);
    }
    return acc_out;
}