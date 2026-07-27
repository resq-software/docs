# Type Alias: CarouselApi

&gt; **CarouselApi** = `UseEmblaCarouselType`\[`1`\]

Defined in: [packages/ui/src/components/carousel/carousel.tsx:50](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/carousel/carousel.tsx#L50)

The Embla carousel instance handed back via the [Carousel](../functions/Carousel) `setApi`
callback — the imperative handle for programmatic control (`scrollNext`,
`scrollTo`, `on`, …).

Is `undefined` until Embla has initialized the viewport, so guard every call
(`api?.scrollNext()`); `setApi` is invoked once the instance becomes available.
