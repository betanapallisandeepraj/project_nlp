#include <wchar.h>
#include <locale.h>
#include <stdio.h>

int main() {
    setlocale(LC_ALL, ""); // Set the locale to use the system's default encoding

    // Telugu Unicode consonant and vowel
    unsigned int teluguConsonant = 0x0C15;  // Example: Consonant "క"
    //unsigned int teluguVowel = 0x0C02;	// Example: Vowel Sign Am
    unsigned int teluguVowel = 0x0C03;      // Example: Vowel Sign Aha

    // Join consonant and vowel to form a word
    unsigned int teluguWord[3];
    teluguWord[0] = teluguConsonant;
    teluguWord[1] = teluguVowel;
    teluguWord[2] = 0;  // Null-terminate the string

    // Display Telugu word
    wprintf(L"Telugu Word: %ls\n", teluguWord);

    return 0;
}

