# Interface: SearchStats

Defined in: [rabin-karp.ts:66](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/rabin-karp.ts#L66)

Statistics gathered during a single search operation.

## Properties

### charactersProcessed

&gt; **charactersProcessed**: `number`

Defined in: [rabin-karp.ts:68](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/rabin-karp.ts#L68)

Total characters processed

***

### hashCollisions

&gt; **hashCollisions**: `number`

Defined in: [rabin-karp.ts:70](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/rabin-karp.ts#L70)

Number of hash collisions (false positives checked)

***

### matchesFound

&gt; **matchesFound**: `number`

Defined in: [rabin-karp.ts:72](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/rabin-karp.ts#L72)

Number of matches found

***

### timeTakenMs

&gt; **timeTakenMs**: `number`

Defined in: [rabin-karp.ts:74](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/rabin-karp.ts#L74)

Time taken in milliseconds
