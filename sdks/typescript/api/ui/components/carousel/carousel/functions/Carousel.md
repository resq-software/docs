# Function: Carousel()

&gt; **Carousel**(`__namedParameters`): `Element`

Defined in: [packages/ui/src/components/carousel/carousel.tsx:80](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/carousel/carousel.tsx#L80)

Root of the carousel — initializes Embla, tracks scroll state, and provides
it to descendants via context. Forwards `opts`/`plugins` to Embla and exposes
the instance through `setApi` for programmatic control.

## Parameters

### \_\_namedParameters

`CarouselProps` & `ClassAttributes`\<`HTMLDivElement`\> & `HTMLAttributes`\<`HTMLDivElement`\>

## Returns

`Element`

## See

[useCarousel](./useCarousel)
