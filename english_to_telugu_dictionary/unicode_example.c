#include <wchar.h>
#include <locale.h>
#include <stdio.h>

int main() {
    setlocale(LC_ALL, ""); // Set the locale to use the system's default encoding

    // Unicode string
    wchar_t unicodeString[] = L"తెలుగు"; // Example Telugu Unicode string

    // Display Unicode string
    wprintf(L"Unicode String: %ls\n", unicodeString);

    return 0;
}

