function analizarConsumo(consumos) {

    // Para contar días con consumo alto mayor que 30 kWh
    let diasAltos = 0;

    for (let i = 0; i < consumos.length; i++) {
        if (consumos[i] > 30) {
            diasAltos++;
        }
    }

    // Para consumo total
    let total = 0;

    for (let i = 0; i < consumos.length; i++) {
        total += consumos[i];
    }

    // Para consumo mínimo
    let minimo = consumos[0];

    for (let i = 1; i < consumos.length; i++) {
        if (consumos[i] < minimo) {
            minimo = consumos[i];
        }
    }

    // Devolver resultado en el orden solicitado
    return [diasAltos, total, minimo];
}

//Hasta aquí para llamar a la función desde consola añadiendo los valores

//Como no me ha quedado claro si ya debe de estar almacenados en un array los valores, si es así, sería a continuación:
// Almacenar valores
let resultado = analizarConsumo([10, 35, 22, 40, 18]); 

//Mostrar el resultado en consola
console.log(resultado);