/*
Author: Sai Suman Chitturi
Created: 2023-08-30 11:59:24
Contest: August Long 2023 Division 2 (Unrated)
Problem: https://www.codechef.com/AUG23B/problems/KDELI

Scraped using https://github.com/ChitturiSaiSuman/Competitive-Companion-for-CodeChef-and-Codeforces
*/

#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>
// #include <ext/pb_ds/assoc_container.hpp>
// #include <boost/multiprecision/cpp_int.hpp>

using namespace std;
// using namespace __gnu_pbds;
// using namespace boost::multiprecision;

#ifdef SUMAN
#include "DEBUG.h"
#define LINE		cerr << "line " << __LINE__ << ": ";
#define debug(x)    LINE; cerr << "(" << #x << ")"; debug(x)
#else
#define debug(x)
#endif

#define FOR(x, N)	for(int x = 0; x < N; x++)
#define endl		'\n'

typedef unsigned long long int ull;
typedef long long int ll;

const short int dc[] = {1, 0, 0, -1, -1, -1, 1, 1};
const short int dr[] = {0, 1, -1, 0, -1, 1, -1, 1};

const ll shit	= ((ll)(998244353));
const ll mod	= ((ll)(1e9 + 7));
const ll hell	= ((ll)(1e9 + 9));
const ll inf	= ((ll)(1e18 + 3));

static inline ll gcd(ll a, ll b) {
	for(; b > 0; a %= b, swap(a, b));
	return a;
}
static inline ll lcm(ll a, ll b) {
	return (a / gcd(a, b)) * b;
}
static inline ll power(ll a, ll b, ll p) {
	ll result = 1;
	for(; b > 0; b >>= 1, a = a * a % p) {
		if(b & 1) {
			result = result * a % p;
		}
	}
	return result;
}
static inline ll inverse(ll a, ll p) {
	return power(a, p - 2, p);
}

#define nax 2000003


void pre_compute() {
	return;
}

void solve() {
	int N = 0, K = 0, L = 0;
	cin >> N >> K >> L;
	vector<int> arr(N);
	for(int _i = 0, _n = arr.size(); _i < _n; _i++) {
		cin >> arr[_i];
	}
	ll ans = 0;
	sort(arr.begin(), arr.end(), greater<int>());
	for (int i = 0; i + L - 1 < N; i += K) {
		ans += arr[i + L - 1];
	}
	cout << ans << '\n';
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int t = 1;
	cin >> t;
	pre_compute();
	FOR(test, t) {
		// cout << "Case #" << (test + 1) << ": ";
		solve();
		#ifdef SUMAN
		cerr << '\n';
		#endif
	}
	return 0;
}