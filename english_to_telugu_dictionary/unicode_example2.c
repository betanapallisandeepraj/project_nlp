#include <wchar.h>
#include <locale.h>
#include <stdio.h>

int main() {
    setlocale(LC_ALL, ""); // Set the locale to use the system's default encoding

    // Telugu Unicode consonant and vowel
    wchar_t teluguConsonant = L'\u0C15';  // Example: Consonant "క"
    wchar_t teluguVowel = L'\u0C3E';      // Example: Vowel Sign "ా"

    // Join consonant and vowel to form a word
    wchar_t teluguWord[3];
    teluguWord[0] = teluguConsonant;
    teluguWord[1] = teluguVowel;
    teluguWord[2] = L'\0';  // Null-terminate the string

    // Display Telugu word
    wprintf(L"Telugu Word: %ls\n", teluguWord);

    return 0;
}

