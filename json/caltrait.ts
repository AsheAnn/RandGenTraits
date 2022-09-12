import body from './body3.json' assert {type: 'json'}
// const body = require('./body3.json')

const bodyJson = JSON.stringify(body)
const seed = body.seed
const trait = body.traits
const traitType = trait[0].type

const subCalculated = [...new Array(traitType.length)].map((_val, index) => {
  const countType = traitType[index]
  const typePercent = countType.percent
  const finalCount = [...new Array(countType.color.length)].map((_val, index) => {
    const indexPercent = countType.color[index].percent
    return seed * typePercent * indexPercent / 10000
  })
  const sum = finalCount.reduce((a, b) => a + b)
  return finalCount 
})


const finalList = [...new Array(subCalculated.length)].map((_val, index) => {
  return subCalculated[index] 
})


// console.log(finalList);
console.log(subCalculated);

