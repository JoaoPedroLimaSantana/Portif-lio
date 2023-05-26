#include <stdio.h>

int main()
{
	int anoatual=2023, anonasc=0, idade=0;
	printf("digite seu ano de nascimento :");
	scanf("%d", &anonasc);
	idade=anoatual-anonasc;
	printf("sua idade e: %d\n", idade);
	printf("\n");
	if (idade >= 18){
		printf("vai trabalhar");
		}
	else{
		printf("estuda");
	}
	return 0;
}
