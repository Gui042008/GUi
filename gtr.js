const furiaCS = ["FalleN", "chelo", "skullz", "yuurih", "KSCERATO"];

// 1) Use a função .indexOf para armazenar o índice do jogador "chelo"
const indexChelo = furiaCS.indexOf("chelo");
console.log("Índice do jogador 'chelo':", indexChelo);

// 2) Usando a função .splice, substitua "chelo" e "skullz" por "molodoy" e "YEKINDAR"
// ** Use o índice encontrado na questão 1
furiaCS.splice(indexChelo, 2, "molodoy", "YEKINDAR");
console.log("Lista após substituições:", furiaCS);

// 3) Usando a função .map, crie uma lista com os caracteres maiúsculos (usar .toUpperCase)
const upperCaseNames = furiaCS.map(name => name.toUpperCase());
console.log("Nomes em maiúsculas:", upperCaseNames);

// 4) Usando a função .sort, ordene a lista com os nomes maiúsculos
const sortedUpperCaseNames = upperCaseNames.sort();
console.log("Nomes em maiúsculas ordenados:", sortedUpperCaseNames);

// 5) Usando a função .filter, filtre apenas os nomes que começam com "y"
const namesStartingWithY = furiaCS.filter(name => name.toLowerCase().startsWith("y"));
console.log("Nomes que começam com 'y':", namesStartingWithY);
