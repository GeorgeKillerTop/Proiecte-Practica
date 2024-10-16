#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
using namespace std;
void actualizeaza_cuvantul_mascat(string& cuvant_mascat, const string& cuvant_complet, char litera_ghicita)
{
    for (size_t i = 0; i < cuvant_complet.length(); ++i)
    {
        if (cuvant_mascat[i] == '*' && cuvant_complet[i] == litera_ghicita)
        {
            cuvant_mascat[i] = litera_ghicita;
        }
    }
}
int ghiceste_litere(string& cuvant_mascat, const string& cuvant_complet)
{
    unordered_set<char> litere_ghicite;
    int numar_incercari = 0;
    unordered_map<char, int> frecventa_litere;
    for (char litera : cuvant_complet)
    {
        frecventa_litere[litera]++;
    }
    vector<pair<char, int>> litere_sortate(frecventa_litere.begin(), frecventa_litere.end());
    sort(litere_sortate.begin(), litere_sortate.end(), [](const auto& a, const auto& b)
    {
        return a.second > b.second;
    });
    for (const auto& pair : litere_sortate)
    {
        char litera = pair.first;
        if (litere_ghicite.find(litera) == litere_ghicite.end() && cuvant_mascat.find(litera) == string::npos)
        {
            numar_incercari++;
            litere_ghicite.insert(litera);
            actualizeaza_cuvantul_mascat(cuvant_mascat, cuvant_complet, litera);
        }
        if (cuvant_mascat == cuvant_complet)
        {
            break;
        }
    }
    return numar_incercari;
}
int main()
{
    ifstream fisier(cuvinte_de_verificat.txt);
    string rand;
    int total_incercari = 0;
    while (getline(fisier, rand))
    {
        istringstream ss(rand);
        string cod_joc, cuvant_mascat, cuvant_complet;
        getline(ss, cod_joc, ';');
        getline(ss, cuvant_mascat, ';');
        getline(ss, cuvant_complet);

        total_incercari += ghiceste_litere(cuvant_mascat, cuvant_complet);
    }
    cout << "\nNumarul total de incercări pentru toate jocurile: " << total_incercari << endl;
    return 0;
}


