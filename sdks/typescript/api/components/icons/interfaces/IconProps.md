# Interface: IconProps

Defined in: node\_modules/@phosphor-icons/react/dist/lib/types.d.ts:3

ResQ icon system — powered by @phosphor-icons/react.

All icons follow the Phosphor naming convention (`*Icon` suffix).
The `weight` prop controls stroke weight: "thin" | "light" | "regular" | "bold" | "fill" | "duotone".
Default weight is "light" (matches the ResQ design system baseline).

Re-exported types:
- `Icon`       — the base ForwardRefExoticComponent type for all icons
- `IconProps`  — props accepted by every icon (weight, size, color, className, …)
- `IconWeight` — the union of allowed weight strings

Server Components: import from `@resq-sw/ui/icons/ssr` instead to avoid
the React.createContext call at module-init time.

## Extends

- `ComponentPropsWithoutRef`\<`"svg"`\>.`RefAttributes`\<`SVGSVGElement`\>

## Properties

### accentHeight?

> `optional` **accentHeight?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3624

#### Inherited from

`ComponentPropsWithoutRef.accentHeight`

***

### accumulate?

> `optional` **accumulate?**: `"none"` \| `"sum"`

Defined in: node\_modules/@types/react/index.d.ts:3625

#### Inherited from

`ComponentPropsWithoutRef.accumulate`

***

### additive?

> `optional` **additive?**: `"replace"` \| `"sum"`

Defined in: node\_modules/@types/react/index.d.ts:3626

#### Inherited from

`ComponentPropsWithoutRef.additive`

***

### alignmentBaseline?

> `optional` **alignmentBaseline?**: `"inherit"` \| `"auto"` \| `"alphabetic"` \| `"hanging"` \| `"ideographic"` \| `"mathematical"` \| `"baseline"` \| `"central"` \| `"middle"` \| `"text-after-edge"` \| `"text-before-edge"` \| `"before-edge"` \| `"after-edge"`

Defined in: node\_modules/@types/react/index.d.ts:3627

#### Inherited from

`ComponentPropsWithoutRef.alignmentBaseline`

***

### allowReorder?

> `optional` **allowReorder?**: `"yes"` \| `"no"`

Defined in: node\_modules/@types/react/index.d.ts:3642

#### Inherited from

`ComponentPropsWithoutRef.allowReorder`

***

### alphabetic?

> `optional` **alphabetic?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3643

#### Inherited from

`ComponentPropsWithoutRef.alphabetic`

***

### alt?

> `optional` **alt?**: `string`

Defined in: node\_modules/@phosphor-icons/react/dist/lib/types.d.ts:4

***

### amplitude?

> `optional` **amplitude?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3644

#### Inherited from

`ComponentPropsWithoutRef.amplitude`

***

### arabicForm?

> `optional` **arabicForm?**: `"initial"` \| `"medial"` \| `"terminal"` \| `"isolated"`

Defined in: node\_modules/@types/react/index.d.ts:3645

#### Inherited from

`ComponentPropsWithoutRef.arabicForm`

***

### aria-activedescendant?

> `optional` **aria-activedescendant?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2491

Identifies the currently active element when DOM focus is on a composite widget, textbox, group, or application.

#### Inherited from

`ComponentPropsWithoutRef.aria-activedescendant`

***

### aria-atomic?

> `optional` **aria-atomic?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:2493

Indicates whether assistive technologies will present all, or only parts of, the changed region based on the change notifications defined by the aria-relevant attribute.

#### Inherited from

`ComponentPropsWithoutRef.aria-atomic`

***

### aria-autocomplete?

> `optional` **aria-autocomplete?**: `"none"` \| `"list"` \| `"inline"` \| `"both"`

Defined in: node\_modules/@types/react/index.d.ts:2498

Indicates whether inputting text could trigger display of one or more predictions of the user's intended value for an input and specifies how predictions would be
presented if they are made.

#### Inherited from

`ComponentPropsWithoutRef.aria-autocomplete`

***

### aria-braillelabel?

> `optional` **aria-braillelabel?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2504

Defines a string value that labels the current element, which is intended to be converted into Braille.

#### See

aria-label.

#### Inherited from

`ComponentPropsWithoutRef.aria-braillelabel`

***

### aria-brailleroledescription?

> `optional` **aria-brailleroledescription?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2509

Defines a human-readable, author-localized abbreviated description for the role of an element, which is intended to be converted into Braille.

#### See

aria-roledescription.

#### Inherited from

`ComponentPropsWithoutRef.aria-brailleroledescription`

***

### aria-busy?

> `optional` **aria-busy?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:2510

#### Inherited from

`ComponentPropsWithoutRef.aria-busy`

***

### aria-checked?

> `optional` **aria-checked?**: `boolean` \| `"true"` \| `"false"` \| `"mixed"`

Defined in: node\_modules/@types/react/index.d.ts:2515

Indicates the current "checked" state of checkboxes, radio buttons, and other widgets.

#### See

 - aria-pressed
 - aria-selected.

#### Inherited from

`ComponentPropsWithoutRef.aria-checked`

***

### aria-colcount?

> `optional` **aria-colcount?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:2520

Defines the total number of columns in a table, grid, or treegrid.

#### See

aria-colindex.

#### Inherited from

`ComponentPropsWithoutRef.aria-colcount`

***

### aria-colindex?

> `optional` **aria-colindex?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:2525

Defines an element's column index or position with respect to the total number of columns within a table, grid, or treegrid.

#### See

 - aria-colcount
 - aria-colspan.

#### Inherited from

`ComponentPropsWithoutRef.aria-colindex`

***

### aria-colindextext?

> `optional` **aria-colindextext?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2530

Defines a human readable text alternative of aria-colindex.

#### See

aria-rowindextext.

#### Inherited from

`ComponentPropsWithoutRef.aria-colindextext`

***

### aria-colspan?

> `optional` **aria-colspan?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:2535

Defines the number of columns spanned by a cell or gridcell within a table, grid, or treegrid.

#### See

 - aria-colindex
 - aria-rowspan.

#### Inherited from

`ComponentPropsWithoutRef.aria-colspan`

***

### aria-controls?

> `optional` **aria-controls?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2540

Identifies the element (or elements) whose contents or presence are controlled by the current element.

#### See

aria-owns.

#### Inherited from

`ComponentPropsWithoutRef.aria-controls`

***

### aria-current?

> `optional` **aria-current?**: `boolean` \| `"time"` \| `"true"` \| `"false"` \| `"page"` \| `"step"` \| `"location"` \| `"date"`

Defined in: node\_modules/@types/react/index.d.ts:2542

Indicates the element that represents the current item within a container or set of related elements.

#### Inherited from

`ComponentPropsWithoutRef.aria-current`

***

### aria-describedby?

> `optional` **aria-describedby?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2547

Identifies the element (or elements) that describes the object.

#### See

aria-labelledby

#### Inherited from

`ComponentPropsWithoutRef.aria-describedby`

***

### aria-description?

> `optional` **aria-description?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2552

Defines a string value that describes or annotates the current element.

#### See

related aria-describedby.

#### Inherited from

`ComponentPropsWithoutRef.aria-description`

***

### aria-details?

> `optional` **aria-details?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2557

Identifies the element that provides a detailed, extended description for the object.

#### See

aria-describedby.

#### Inherited from

`ComponentPropsWithoutRef.aria-details`

***

### aria-disabled?

> `optional` **aria-disabled?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:2562

Indicates that the element is perceivable but disabled, so it is not editable or otherwise operable.

#### See

 - aria-hidden
 - aria-readonly.

#### Inherited from

`ComponentPropsWithoutRef.aria-disabled`

***

### ~~aria-dropeffect?~~

> `optional` **aria-dropeffect?**: `"link"` \| `"none"` \| `"copy"` \| `"execute"` \| `"move"` \| `"popup"`

Defined in: node\_modules/@types/react/index.d.ts:2567

Indicates what functions can be performed when a dragged object is released on the drop target.

#### Deprecated

in ARIA 1.1

#### Inherited from

`ComponentPropsWithoutRef.aria-dropeffect`

***

### aria-errormessage?

> `optional` **aria-errormessage?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2572

Identifies the element that provides an error message for the object.

#### See

 - aria-invalid
 - aria-describedby.

#### Inherited from

`ComponentPropsWithoutRef.aria-errormessage`

***

### aria-expanded?

> `optional` **aria-expanded?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:2574

Indicates whether the element, or another grouping element it controls, is currently expanded or collapsed.

#### Inherited from

`ComponentPropsWithoutRef.aria-expanded`

***

### aria-flowto?

> `optional` **aria-flowto?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2579

Identifies the next element (or elements) in an alternate reading order of content which, at the user's discretion,
allows assistive technology to override the general default of reading in document source order.

#### Inherited from

`ComponentPropsWithoutRef.aria-flowto`

***

### ~~aria-grabbed?~~

> `optional` **aria-grabbed?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:2584

Indicates an element's "grabbed" state in a drag-and-drop operation.

#### Deprecated

in ARIA 1.1

#### Inherited from

`ComponentPropsWithoutRef.aria-grabbed`

***

### aria-haspopup?

> `optional` **aria-haspopup?**: `boolean` \| `"dialog"` \| `"menu"` \| `"true"` \| `"false"` \| `"grid"` \| `"listbox"` \| `"tree"`

Defined in: node\_modules/@types/react/index.d.ts:2586

Indicates the availability and type of interactive popup element, such as menu or dialog, that can be triggered by an element.

#### Inherited from

`ComponentPropsWithoutRef.aria-haspopup`

***

### aria-hidden?

> `optional` **aria-hidden?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:2591

Indicates whether the element is exposed to an accessibility API.

#### See

aria-disabled.

#### Inherited from

`ComponentPropsWithoutRef.aria-hidden`

***

### aria-invalid?

> `optional` **aria-invalid?**: `boolean` \| `"true"` \| `"false"` \| `"grammar"` \| `"spelling"`

Defined in: node\_modules/@types/react/index.d.ts:2596

Indicates the entered value does not conform to the format expected by the application.

#### See

aria-errormessage.

#### Inherited from

`ComponentPropsWithoutRef.aria-invalid`

***

### aria-keyshortcuts?

> `optional` **aria-keyshortcuts?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2598

Indicates keyboard shortcuts that an author has implemented to activate or give focus to an element.

#### Inherited from

`ComponentPropsWithoutRef.aria-keyshortcuts`

***

### aria-label?

> `optional` **aria-label?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2603

Defines a string value that labels the current element.

#### See

aria-labelledby.

#### Inherited from

`ComponentPropsWithoutRef.aria-label`

***

### aria-labelledby?

> `optional` **aria-labelledby?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2608

Identifies the element (or elements) that labels the current element.

#### See

aria-describedby.

#### Inherited from

`ComponentPropsWithoutRef.aria-labelledby`

***

### aria-level?

> `optional` **aria-level?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:2610

Defines the hierarchical level of an element within a structure.

#### Inherited from

`ComponentPropsWithoutRef.aria-level`

***

### aria-live?

> `optional` **aria-live?**: `"off"` \| `"assertive"` \| `"polite"`

Defined in: node\_modules/@types/react/index.d.ts:2612

Indicates that an element will be updated, and describes the types of updates the user agents, assistive technologies, and user can expect from the live region.

#### Inherited from

`ComponentPropsWithoutRef.aria-live`

***

### aria-modal?

> `optional` **aria-modal?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:2614

Indicates whether an element is modal when displayed.

#### Inherited from

`ComponentPropsWithoutRef.aria-modal`

***

### aria-multiline?

> `optional` **aria-multiline?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:2616

Indicates whether a text box accepts multiple lines of input or only a single line.

#### Inherited from

`ComponentPropsWithoutRef.aria-multiline`

***

### aria-multiselectable?

> `optional` **aria-multiselectable?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:2618

Indicates that the user may select more than one item from the current selectable descendants.

#### Inherited from

`ComponentPropsWithoutRef.aria-multiselectable`

***

### aria-orientation?

> `optional` **aria-orientation?**: `"horizontal"` \| `"vertical"`

Defined in: node\_modules/@types/react/index.d.ts:2620

Indicates whether the element's orientation is horizontal, vertical, or unknown/ambiguous.

#### Inherited from

`ComponentPropsWithoutRef.aria-orientation`

***

### aria-owns?

> `optional` **aria-owns?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2626

Identifies an element (or elements) in order to define a visual, functional, or contextual parent/child relationship
between DOM elements where the DOM hierarchy cannot be used to represent the relationship.

#### See

aria-controls.

#### Inherited from

`ComponentPropsWithoutRef.aria-owns`

***

### aria-placeholder?

> `optional` **aria-placeholder?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2631

Defines a short hint (a word or short phrase) intended to aid the user with data entry when the control has no value.
A hint could be a sample value or a brief description of the expected format.

#### Inherited from

`ComponentPropsWithoutRef.aria-placeholder`

***

### aria-posinset?

> `optional` **aria-posinset?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:2636

Defines an element's number or position in the current set of listitems or treeitems. Not required if all elements in the set are present in the DOM.

#### See

aria-setsize.

#### Inherited from

`ComponentPropsWithoutRef.aria-posinset`

***

### aria-pressed?

> `optional` **aria-pressed?**: `boolean` \| `"true"` \| `"false"` \| `"mixed"`

Defined in: node\_modules/@types/react/index.d.ts:2641

Indicates the current "pressed" state of toggle buttons.

#### See

 - aria-checked
 - aria-selected.

#### Inherited from

`ComponentPropsWithoutRef.aria-pressed`

***

### aria-readonly?

> `optional` **aria-readonly?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:2646

Indicates that the element is not editable, but is otherwise operable.

#### See

aria-disabled.

#### Inherited from

`ComponentPropsWithoutRef.aria-readonly`

***

### aria-relevant?

> `optional` **aria-relevant?**: `"text"` \| `"additions"` \| `"additions removals"` \| `"additions text"` \| `"all"` \| `"removals"` \| `"removals additions"` \| `"removals text"` \| `"text additions"` \| `"text removals"`

Defined in: node\_modules/@types/react/index.d.ts:2651

Indicates what notifications the user agent will trigger when the accessibility tree within a live region is modified.

#### See

aria-atomic.

#### Inherited from

`ComponentPropsWithoutRef.aria-relevant`

***

### aria-required?

> `optional` **aria-required?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:2664

Indicates that user input is required on the element before a form may be submitted.

#### Inherited from

`ComponentPropsWithoutRef.aria-required`

***

### aria-roledescription?

> `optional` **aria-roledescription?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2666

Defines a human-readable, author-localized description for the role of an element.

#### Inherited from

`ComponentPropsWithoutRef.aria-roledescription`

***

### aria-rowcount?

> `optional` **aria-rowcount?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:2671

Defines the total number of rows in a table, grid, or treegrid.

#### See

aria-rowindex.

#### Inherited from

`ComponentPropsWithoutRef.aria-rowcount`

***

### aria-rowindex?

> `optional` **aria-rowindex?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:2676

Defines an element's row index or position with respect to the total number of rows within a table, grid, or treegrid.

#### See

 - aria-rowcount
 - aria-rowspan.

#### Inherited from

`ComponentPropsWithoutRef.aria-rowindex`

***

### aria-rowindextext?

> `optional` **aria-rowindextext?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2681

Defines a human readable text alternative of aria-rowindex.

#### See

aria-colindextext.

#### Inherited from

`ComponentPropsWithoutRef.aria-rowindextext`

***

### aria-rowspan?

> `optional` **aria-rowspan?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:2686

Defines the number of rows spanned by a cell or gridcell within a table, grid, or treegrid.

#### See

 - aria-rowindex
 - aria-colspan.

#### Inherited from

`ComponentPropsWithoutRef.aria-rowspan`

***

### aria-selected?

> `optional` **aria-selected?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:2691

Indicates the current "selected" state of various widgets.

#### See

 - aria-checked
 - aria-pressed.

#### Inherited from

`ComponentPropsWithoutRef.aria-selected`

***

### aria-setsize?

> `optional` **aria-setsize?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:2696

Defines the number of items in the current set of listitems or treeitems. Not required if all elements in the set are present in the DOM.

#### See

aria-posinset.

#### Inherited from

`ComponentPropsWithoutRef.aria-setsize`

***

### aria-sort?

> `optional` **aria-sort?**: `"none"` \| `"ascending"` \| `"descending"` \| `"other"`

Defined in: node\_modules/@types/react/index.d.ts:2698

Indicates if items in a table or grid are sorted in ascending or descending order.

#### Inherited from

`ComponentPropsWithoutRef.aria-sort`

***

### aria-valuemax?

> `optional` **aria-valuemax?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:2700

Defines the maximum allowed value for a range widget.

#### Inherited from

`ComponentPropsWithoutRef.aria-valuemax`

***

### aria-valuemin?

> `optional` **aria-valuemin?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:2702

Defines the minimum allowed value for a range widget.

#### Inherited from

`ComponentPropsWithoutRef.aria-valuemin`

***

### aria-valuenow?

> `optional` **aria-valuenow?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:2707

Defines the current value for a range widget.

#### See

aria-valuetext.

#### Inherited from

`ComponentPropsWithoutRef.aria-valuenow`

***

### aria-valuetext?

> `optional` **aria-valuetext?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:2709

Defines the human readable text alternative of aria-valuenow for a range widget.

#### Inherited from

`ComponentPropsWithoutRef.aria-valuetext`

***

### ascent?

> `optional` **ascent?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3646

#### Inherited from

`ComponentPropsWithoutRef.ascent`

***

### attributeName?

> `optional` **attributeName?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3647

#### Inherited from

`ComponentPropsWithoutRef.attributeName`

***

### attributeType?

> `optional` **attributeType?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3648

#### Inherited from

`ComponentPropsWithoutRef.attributeType`

***

### autoReverse?

> `optional` **autoReverse?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:3649

#### Inherited from

`ComponentPropsWithoutRef.autoReverse`

***

### azimuth?

> `optional` **azimuth?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3650

#### Inherited from

`ComponentPropsWithoutRef.azimuth`

***

### baseFrequency?

> `optional` **baseFrequency?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3651

#### Inherited from

`ComponentPropsWithoutRef.baseFrequency`

***

### baselineShift?

> `optional` **baselineShift?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3652

#### Inherited from

`ComponentPropsWithoutRef.baselineShift`

***

### baseProfile?

> `optional` **baseProfile?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3653

#### Inherited from

`ComponentPropsWithoutRef.baseProfile`

***

### bbox?

> `optional` **bbox?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3654

#### Inherited from

`ComponentPropsWithoutRef.bbox`

***

### begin?

> `optional` **begin?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3655

#### Inherited from

`ComponentPropsWithoutRef.begin`

***

### bias?

> `optional` **bias?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3656

#### Inherited from

`ComponentPropsWithoutRef.bias`

***

### by?

> `optional` **by?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3657

#### Inherited from

`ComponentPropsWithoutRef.by`

***

### calcMode?

> `optional` **calcMode?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3658

#### Inherited from

`ComponentPropsWithoutRef.calcMode`

***

### capHeight?

> `optional` **capHeight?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3659

#### Inherited from

`ComponentPropsWithoutRef.capHeight`

***

### children?

> `optional` **children?**: `ReactNode`

Defined in: node\_modules/@types/react/index.d.ts:2267

#### Inherited from

`ComponentPropsWithoutRef.children`

***

### className?

> `optional` **className?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3600

#### Inherited from

`ComponentPropsWithoutRef.className`

***

### clip?

> `optional` **clip?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3660

#### Inherited from

`ComponentPropsWithoutRef.clip`

***

### clipPath?

> `optional` **clipPath?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3661

#### Inherited from

`ComponentPropsWithoutRef.clipPath`

***

### clipPathUnits?

> `optional` **clipPathUnits?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3662

#### Inherited from

`ComponentPropsWithoutRef.clipPathUnits`

***

### clipRule?

> `optional` **clipRule?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3663

#### Inherited from

`ComponentPropsWithoutRef.clipRule`

***

### color?

> `optional` **color?**: `string`

Defined in: node\_modules/@phosphor-icons/react/dist/lib/types.d.ts:5

#### Overrides

`ComponentPropsWithoutRef.color`

***

### colorInterpolation?

> `optional` **colorInterpolation?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3664

#### Inherited from

`ComponentPropsWithoutRef.colorInterpolation`

***

### colorInterpolationFilters?

> `optional` **colorInterpolationFilters?**: `"inherit"` \| `"auto"` \| `"linearRGB"` \| `"sRGB"`

Defined in: node\_modules/@types/react/index.d.ts:3665

#### Inherited from

`ComponentPropsWithoutRef.colorInterpolationFilters`

***

### colorProfile?

> `optional` **colorProfile?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3666

#### Inherited from

`ComponentPropsWithoutRef.colorProfile`

***

### colorRendering?

> `optional` **colorRendering?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3667

#### Inherited from

`ComponentPropsWithoutRef.colorRendering`

***

### contentScriptType?

> `optional` **contentScriptType?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3668

#### Inherited from

`ComponentPropsWithoutRef.contentScriptType`

***

### contentStyleType?

> `optional` **contentStyleType?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3669

#### Inherited from

`ComponentPropsWithoutRef.contentStyleType`

***

### crossOrigin?

> `optional` **crossOrigin?**: `CrossOrigin`

Defined in: node\_modules/@types/react/index.d.ts:3621

#### Inherited from

`ComponentPropsWithoutRef.crossOrigin`

***

### cursor?

> `optional` **cursor?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3670

#### Inherited from

`ComponentPropsWithoutRef.cursor`

***

### cx?

> `optional` **cx?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3671

#### Inherited from

`ComponentPropsWithoutRef.cx`

***

### cy?

> `optional` **cy?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3672

#### Inherited from

`ComponentPropsWithoutRef.cy`

***

### d?

> `optional` **d?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3673

#### Inherited from

`ComponentPropsWithoutRef.d`

***

### dangerouslySetInnerHTML?

> `optional` **dangerouslySetInnerHTML?**: `object`

Defined in: node\_modules/@types/react/index.d.ts:2268

#### \_\_html

> **\_\_html**: `string` \| `TrustedHTML`

#### Inherited from

`ComponentPropsWithoutRef.dangerouslySetInnerHTML`

***

### decelerate?

> `optional` **decelerate?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3674

#### Inherited from

`ComponentPropsWithoutRef.decelerate`

***

### descent?

> `optional` **descent?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3675

#### Inherited from

`ComponentPropsWithoutRef.descent`

***

### diffuseConstant?

> `optional` **diffuseConstant?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3676

#### Inherited from

`ComponentPropsWithoutRef.diffuseConstant`

***

### direction?

> `optional` **direction?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3677

#### Inherited from

`ComponentPropsWithoutRef.direction`

***

### display?

> `optional` **display?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3678

#### Inherited from

`ComponentPropsWithoutRef.display`

***

### divisor?

> `optional` **divisor?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3679

#### Inherited from

`ComponentPropsWithoutRef.divisor`

***

### dominantBaseline?

> `optional` **dominantBaseline?**: `"inherit"` \| `"auto"` \| `"alphabetic"` \| `"hanging"` \| `"ideographic"` \| `"mathematical"` \| `"central"` \| `"middle"` \| `"text-after-edge"` \| `"text-before-edge"` \| `"use-script"` \| `"no-change"` \| `"reset-size"`

Defined in: node\_modules/@types/react/index.d.ts:3680

#### Inherited from

`ComponentPropsWithoutRef.dominantBaseline`

***

### dur?

> `optional` **dur?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3695

#### Inherited from

`ComponentPropsWithoutRef.dur`

***

### dx?

> `optional` **dx?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3696

#### Inherited from

`ComponentPropsWithoutRef.dx`

***

### dy?

> `optional` **dy?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3697

#### Inherited from

`ComponentPropsWithoutRef.dy`

***

### edgeMode?

> `optional` **edgeMode?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3698

#### Inherited from

`ComponentPropsWithoutRef.edgeMode`

***

### elevation?

> `optional` **elevation?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3699

#### Inherited from

`ComponentPropsWithoutRef.elevation`

***

### enableBackground?

> `optional` **enableBackground?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3700

#### Inherited from

`ComponentPropsWithoutRef.enableBackground`

***

### end?

> `optional` **end?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3701

#### Inherited from

`ComponentPropsWithoutRef.end`

***

### exponent?

> `optional` **exponent?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3702

#### Inherited from

`ComponentPropsWithoutRef.exponent`

***

### externalResourcesRequired?

> `optional` **externalResourcesRequired?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:3703

#### Inherited from

`ComponentPropsWithoutRef.externalResourcesRequired`

***

### fill?

> `optional` **fill?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3704

#### Inherited from

`ComponentPropsWithoutRef.fill`

***

### fillOpacity?

> `optional` **fillOpacity?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3705

#### Inherited from

`ComponentPropsWithoutRef.fillOpacity`

***

### fillRule?

> `optional` **fillRule?**: `"inherit"` \| `"evenodd"` \| `"nonzero"`

Defined in: node\_modules/@types/react/index.d.ts:3706

#### Inherited from

`ComponentPropsWithoutRef.fillRule`

***

### filter?

> `optional` **filter?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3707

#### Inherited from

`ComponentPropsWithoutRef.filter`

***

### filterRes?

> `optional` **filterRes?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3708

#### Inherited from

`ComponentPropsWithoutRef.filterRes`

***

### filterUnits?

> `optional` **filterUnits?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3709

#### Inherited from

`ComponentPropsWithoutRef.filterUnits`

***

### floodColor?

> `optional` **floodColor?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3710

#### Inherited from

`ComponentPropsWithoutRef.floodColor`

***

### floodOpacity?

> `optional` **floodOpacity?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3711

#### Inherited from

`ComponentPropsWithoutRef.floodOpacity`

***

### focusable?

> `optional` **focusable?**: `Booleanish` \| `"auto"`

Defined in: node\_modules/@types/react/index.d.ts:3712

#### Inherited from

`ComponentPropsWithoutRef.focusable`

***

### fontFamily?

> `optional` **fontFamily?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3713

#### Inherited from

`ComponentPropsWithoutRef.fontFamily`

***

### fontSize?

> `optional` **fontSize?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3714

#### Inherited from

`ComponentPropsWithoutRef.fontSize`

***

### fontSizeAdjust?

> `optional` **fontSizeAdjust?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3715

#### Inherited from

`ComponentPropsWithoutRef.fontSizeAdjust`

***

### fontStretch?

> `optional` **fontStretch?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3716

#### Inherited from

`ComponentPropsWithoutRef.fontStretch`

***

### fontStyle?

> `optional` **fontStyle?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3717

#### Inherited from

`ComponentPropsWithoutRef.fontStyle`

***

### fontVariant?

> `optional` **fontVariant?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3718

#### Inherited from

`ComponentPropsWithoutRef.fontVariant`

***

### fontWeight?

> `optional` **fontWeight?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3719

#### Inherited from

`ComponentPropsWithoutRef.fontWeight`

***

### format?

> `optional` **format?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3720

#### Inherited from

`ComponentPropsWithoutRef.format`

***

### fr?

> `optional` **fr?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3721

#### Inherited from

`ComponentPropsWithoutRef.fr`

***

### from?

> `optional` **from?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3722

#### Inherited from

`ComponentPropsWithoutRef.from`

***

### fx?

> `optional` **fx?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3723

#### Inherited from

`ComponentPropsWithoutRef.fx`

***

### fy?

> `optional` **fy?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3724

#### Inherited from

`ComponentPropsWithoutRef.fy`

***

### g1?

> `optional` **g1?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3725

#### Inherited from

`ComponentPropsWithoutRef.g1`

***

### g2?

> `optional` **g2?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3726

#### Inherited from

`ComponentPropsWithoutRef.g2`

***

### glyphName?

> `optional` **glyphName?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3727

#### Inherited from

`ComponentPropsWithoutRef.glyphName`

***

### glyphOrientationHorizontal?

> `optional` **glyphOrientationHorizontal?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3728

#### Inherited from

`ComponentPropsWithoutRef.glyphOrientationHorizontal`

***

### glyphOrientationVertical?

> `optional` **glyphOrientationVertical?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3729

#### Inherited from

`ComponentPropsWithoutRef.glyphOrientationVertical`

***

### glyphRef?

> `optional` **glyphRef?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3730

#### Inherited from

`ComponentPropsWithoutRef.glyphRef`

***

### gradientTransform?

> `optional` **gradientTransform?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3731

#### Inherited from

`ComponentPropsWithoutRef.gradientTransform`

***

### gradientUnits?

> `optional` **gradientUnits?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3732

#### Inherited from

`ComponentPropsWithoutRef.gradientUnits`

***

### hanging?

> `optional` **hanging?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3733

#### Inherited from

`ComponentPropsWithoutRef.hanging`

***

### height?

> `optional` **height?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3602

#### Inherited from

`ComponentPropsWithoutRef.height`

***

### horizAdvX?

> `optional` **horizAdvX?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3734

#### Inherited from

`ComponentPropsWithoutRef.horizAdvX`

***

### horizOriginX?

> `optional` **horizOriginX?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3735

#### Inherited from

`ComponentPropsWithoutRef.horizOriginX`

***

### href?

> `optional` **href?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3736

#### Inherited from

`ComponentPropsWithoutRef.href`

***

### id?

> `optional` **id?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3603

#### Inherited from

`ComponentPropsWithoutRef.id`

***

### ideographic?

> `optional` **ideographic?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3737

#### Inherited from

`ComponentPropsWithoutRef.ideographic`

***

### imageRendering?

> `optional` **imageRendering?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3738

#### Inherited from

`ComponentPropsWithoutRef.imageRendering`

***

### in?

> `optional` **in?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3740

#### Inherited from

`ComponentPropsWithoutRef.in`

***

### in2?

> `optional` **in2?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3739

#### Inherited from

`ComponentPropsWithoutRef.in2`

***

### intercept?

> `optional` **intercept?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3741

#### Inherited from

`ComponentPropsWithoutRef.intercept`

***

### k?

> `optional` **k?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3746

#### Inherited from

`ComponentPropsWithoutRef.k`

***

### k1?

> `optional` **k1?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3742

#### Inherited from

`ComponentPropsWithoutRef.k1`

***

### k2?

> `optional` **k2?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3743

#### Inherited from

`ComponentPropsWithoutRef.k2`

***

### k3?

> `optional` **k3?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3744

#### Inherited from

`ComponentPropsWithoutRef.k3`

***

### k4?

> `optional` **k4?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3745

#### Inherited from

`ComponentPropsWithoutRef.k4`

***

### kernelMatrix?

> `optional` **kernelMatrix?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3747

#### Inherited from

`ComponentPropsWithoutRef.kernelMatrix`

***

### kernelUnitLength?

> `optional` **kernelUnitLength?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3748

#### Inherited from

`ComponentPropsWithoutRef.kernelUnitLength`

***

### kerning?

> `optional` **kerning?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3749

#### Inherited from

`ComponentPropsWithoutRef.kerning`

***

### key?

> `optional` **key?**: `Key` \| `null`

Defined in: node\_modules/@types/react/index.d.ts:259

#### Inherited from

`ComponentPropsWithoutRef.key`

***

### keyPoints?

> `optional` **keyPoints?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3750

#### Inherited from

`ComponentPropsWithoutRef.keyPoints`

***

### keySplines?

> `optional` **keySplines?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3751

#### Inherited from

`ComponentPropsWithoutRef.keySplines`

***

### keyTimes?

> `optional` **keyTimes?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3752

#### Inherited from

`ComponentPropsWithoutRef.keyTimes`

***

### lang?

> `optional` **lang?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3604

#### Inherited from

`ComponentPropsWithoutRef.lang`

***

### lengthAdjust?

> `optional` **lengthAdjust?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3753

#### Inherited from

`ComponentPropsWithoutRef.lengthAdjust`

***

### letterSpacing?

> `optional` **letterSpacing?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3754

#### Inherited from

`ComponentPropsWithoutRef.letterSpacing`

***

### lightingColor?

> `optional` **lightingColor?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3755

#### Inherited from

`ComponentPropsWithoutRef.lightingColor`

***

### limitingConeAngle?

> `optional` **limitingConeAngle?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3756

#### Inherited from

`ComponentPropsWithoutRef.limitingConeAngle`

***

### local?

> `optional` **local?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3757

#### Inherited from

`ComponentPropsWithoutRef.local`

***

### markerEnd?

> `optional` **markerEnd?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3758

#### Inherited from

`ComponentPropsWithoutRef.markerEnd`

***

### markerHeight?

> `optional` **markerHeight?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3759

#### Inherited from

`ComponentPropsWithoutRef.markerHeight`

***

### markerMid?

> `optional` **markerMid?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3760

#### Inherited from

`ComponentPropsWithoutRef.markerMid`

***

### markerStart?

> `optional` **markerStart?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3761

#### Inherited from

`ComponentPropsWithoutRef.markerStart`

***

### markerUnits?

> `optional` **markerUnits?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3762

#### Inherited from

`ComponentPropsWithoutRef.markerUnits`

***

### markerWidth?

> `optional` **markerWidth?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3763

#### Inherited from

`ComponentPropsWithoutRef.markerWidth`

***

### mask?

> `optional` **mask?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3764

#### Inherited from

`ComponentPropsWithoutRef.mask`

***

### maskContentUnits?

> `optional` **maskContentUnits?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3765

#### Inherited from

`ComponentPropsWithoutRef.maskContentUnits`

***

### maskUnits?

> `optional` **maskUnits?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3766

#### Inherited from

`ComponentPropsWithoutRef.maskUnits`

***

### mathematical?

> `optional` **mathematical?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3767

#### Inherited from

`ComponentPropsWithoutRef.mathematical`

***

### max?

> `optional` **max?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3605

#### Inherited from

`ComponentPropsWithoutRef.max`

***

### media?

> `optional` **media?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3606

#### Inherited from

`ComponentPropsWithoutRef.media`

***

### method?

> `optional` **method?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3607

#### Inherited from

`ComponentPropsWithoutRef.method`

***

### min?

> `optional` **min?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3608

#### Inherited from

`ComponentPropsWithoutRef.min`

***

### mirrored?

> `optional` **mirrored?**: `boolean`

Defined in: node\_modules/@phosphor-icons/react/dist/lib/types.d.ts:8

***

### mode?

> `optional` **mode?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3768

#### Inherited from

`ComponentPropsWithoutRef.mode`

***

### name?

> `optional` **name?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3609

#### Inherited from

`ComponentPropsWithoutRef.name`

***

### nonce?

> `optional` **nonce?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3610

#### Inherited from

`ComponentPropsWithoutRef.nonce`

***

### numOctaves?

> `optional` **numOctaves?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3769

#### Inherited from

`ComponentPropsWithoutRef.numOctaves`

***

### offset?

> `optional` **offset?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3770

#### Inherited from

`ComponentPropsWithoutRef.offset`

***

### onAbort?

> `optional` **onAbort?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2327

#### Inherited from

`ComponentPropsWithoutRef.onAbort`

***

### onAbortCapture?

> `optional` **onAbortCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2328

#### Inherited from

`ComponentPropsWithoutRef.onAbortCapture`

***

### onAnimationEnd?

> `optional` **onAnimationEnd?**: `AnimationEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2457

#### Inherited from

`ComponentPropsWithoutRef.onAnimationEnd`

***

### onAnimationEndCapture?

> `optional` **onAnimationEndCapture?**: `AnimationEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2458

#### Inherited from

`ComponentPropsWithoutRef.onAnimationEndCapture`

***

### onAnimationIteration?

> `optional` **onAnimationIteration?**: `AnimationEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2459

#### Inherited from

`ComponentPropsWithoutRef.onAnimationIteration`

***

### onAnimationIterationCapture?

> `optional` **onAnimationIterationCapture?**: `AnimationEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2460

#### Inherited from

`ComponentPropsWithoutRef.onAnimationIterationCapture`

***

### onAnimationStart?

> `optional` **onAnimationStart?**: `AnimationEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2455

#### Inherited from

`ComponentPropsWithoutRef.onAnimationStart`

***

### onAnimationStartCapture?

> `optional` **onAnimationStartCapture?**: `AnimationEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2456

#### Inherited from

`ComponentPropsWithoutRef.onAnimationStartCapture`

***

### onAuxClick?

> `optional` **onAuxClick?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2373

#### Inherited from

`ComponentPropsWithoutRef.onAuxClick`

***

### onAuxClickCapture?

> `optional` **onAuxClickCapture?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2374

#### Inherited from

`ComponentPropsWithoutRef.onAuxClickCapture`

***

### onBeforeInput?

> `optional` **onBeforeInput?**: `InputEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2299

#### Inherited from

`ComponentPropsWithoutRef.onBeforeInput`

***

### onBeforeInputCapture?

> `optional` **onBeforeInputCapture?**: `InputEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2300

#### Inherited from

`ComponentPropsWithoutRef.onBeforeInputCapture`

***

### onBeforeToggle?

> `optional` **onBeforeToggle?**: `ToggleEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2464

#### Inherited from

`ComponentPropsWithoutRef.onBeforeToggle`

***

### onBlur?

> `optional` **onBlur?**: `FocusEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2293

#### Inherited from

`ComponentPropsWithoutRef.onBlur`

***

### onBlurCapture?

> `optional` **onBlurCapture?**: `FocusEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2294

#### Inherited from

`ComponentPropsWithoutRef.onBlurCapture`

***

### onCanPlay?

> `optional` **onCanPlay?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2329

#### Inherited from

`ComponentPropsWithoutRef.onCanPlay`

***

### onCanPlayCapture?

> `optional` **onCanPlayCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2330

#### Inherited from

`ComponentPropsWithoutRef.onCanPlayCapture`

***

### onCanPlayThrough?

> `optional` **onCanPlayThrough?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2331

#### Inherited from

`ComponentPropsWithoutRef.onCanPlayThrough`

***

### onCanPlayThroughCapture?

> `optional` **onCanPlayThroughCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2332

#### Inherited from

`ComponentPropsWithoutRef.onCanPlayThroughCapture`

***

### onChange?

> `optional` **onChange?**: `ChangeEventHandler`\<`SVGSVGElement`, `Element`\>

Defined in: node\_modules/@types/react/index.d.ts:2297

#### Inherited from

`ComponentPropsWithoutRef.onChange`

***

### onChangeCapture?

> `optional` **onChangeCapture?**: `ChangeEventHandler`\<`SVGSVGElement`, `Element`\>

Defined in: node\_modules/@types/react/index.d.ts:2298

#### Inherited from

`ComponentPropsWithoutRef.onChangeCapture`

***

### onClick?

> `optional` **onClick?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2375

#### Inherited from

`ComponentPropsWithoutRef.onClick`

***

### onClickCapture?

> `optional` **onClickCapture?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2376

#### Inherited from

`ComponentPropsWithoutRef.onClickCapture`

***

### onCompositionEnd?

> `optional` **onCompositionEnd?**: `CompositionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2283

#### Inherited from

`ComponentPropsWithoutRef.onCompositionEnd`

***

### onCompositionEndCapture?

> `optional` **onCompositionEndCapture?**: `CompositionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2284

#### Inherited from

`ComponentPropsWithoutRef.onCompositionEndCapture`

***

### onCompositionStart?

> `optional` **onCompositionStart?**: `CompositionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2285

#### Inherited from

`ComponentPropsWithoutRef.onCompositionStart`

***

### onCompositionStartCapture?

> `optional` **onCompositionStartCapture?**: `CompositionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2286

#### Inherited from

`ComponentPropsWithoutRef.onCompositionStartCapture`

***

### onCompositionUpdate?

> `optional` **onCompositionUpdate?**: `CompositionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2287

#### Inherited from

`ComponentPropsWithoutRef.onCompositionUpdate`

***

### onCompositionUpdateCapture?

> `optional` **onCompositionUpdateCapture?**: `CompositionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2288

#### Inherited from

`ComponentPropsWithoutRef.onCompositionUpdateCapture`

***

### onContextMenu?

> `optional` **onContextMenu?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2377

#### Inherited from

`ComponentPropsWithoutRef.onContextMenu`

***

### onContextMenuCapture?

> `optional` **onContextMenuCapture?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2378

#### Inherited from

`ComponentPropsWithoutRef.onContextMenuCapture`

***

### onCopy?

> `optional` **onCopy?**: `ClipboardEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2275

#### Inherited from

`ComponentPropsWithoutRef.onCopy`

***

### onCopyCapture?

> `optional` **onCopyCapture?**: `ClipboardEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2276

#### Inherited from

`ComponentPropsWithoutRef.onCopyCapture`

***

### onCut?

> `optional` **onCut?**: `ClipboardEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2277

#### Inherited from

`ComponentPropsWithoutRef.onCut`

***

### onCutCapture?

> `optional` **onCutCapture?**: `ClipboardEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2278

#### Inherited from

`ComponentPropsWithoutRef.onCutCapture`

***

### onDoubleClick?

> `optional` **onDoubleClick?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2379

#### Inherited from

`ComponentPropsWithoutRef.onDoubleClick`

***

### onDoubleClickCapture?

> `optional` **onDoubleClickCapture?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2380

#### Inherited from

`ComponentPropsWithoutRef.onDoubleClickCapture`

***

### onDrag?

> `optional` **onDrag?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2381

#### Inherited from

`ComponentPropsWithoutRef.onDrag`

***

### onDragCapture?

> `optional` **onDragCapture?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2382

#### Inherited from

`ComponentPropsWithoutRef.onDragCapture`

***

### onDragEnd?

> `optional` **onDragEnd?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2383

#### Inherited from

`ComponentPropsWithoutRef.onDragEnd`

***

### onDragEndCapture?

> `optional` **onDragEndCapture?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2384

#### Inherited from

`ComponentPropsWithoutRef.onDragEndCapture`

***

### onDragEnter?

> `optional` **onDragEnter?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2385

#### Inherited from

`ComponentPropsWithoutRef.onDragEnter`

***

### onDragEnterCapture?

> `optional` **onDragEnterCapture?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2386

#### Inherited from

`ComponentPropsWithoutRef.onDragEnterCapture`

***

### onDragExit?

> `optional` **onDragExit?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2387

#### Inherited from

`ComponentPropsWithoutRef.onDragExit`

***

### onDragExitCapture?

> `optional` **onDragExitCapture?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2388

#### Inherited from

`ComponentPropsWithoutRef.onDragExitCapture`

***

### onDragLeave?

> `optional` **onDragLeave?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2389

#### Inherited from

`ComponentPropsWithoutRef.onDragLeave`

***

### onDragLeaveCapture?

> `optional` **onDragLeaveCapture?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2390

#### Inherited from

`ComponentPropsWithoutRef.onDragLeaveCapture`

***

### onDragOver?

> `optional` **onDragOver?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2391

#### Inherited from

`ComponentPropsWithoutRef.onDragOver`

***

### onDragOverCapture?

> `optional` **onDragOverCapture?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2392

#### Inherited from

`ComponentPropsWithoutRef.onDragOverCapture`

***

### onDragStart?

> `optional` **onDragStart?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2393

#### Inherited from

`ComponentPropsWithoutRef.onDragStart`

***

### onDragStartCapture?

> `optional` **onDragStartCapture?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2394

#### Inherited from

`ComponentPropsWithoutRef.onDragStartCapture`

***

### onDrop?

> `optional` **onDrop?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2395

#### Inherited from

`ComponentPropsWithoutRef.onDrop`

***

### onDropCapture?

> `optional` **onDropCapture?**: `DragEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2396

#### Inherited from

`ComponentPropsWithoutRef.onDropCapture`

***

### onDurationChange?

> `optional` **onDurationChange?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2333

#### Inherited from

`ComponentPropsWithoutRef.onDurationChange`

***

### onDurationChangeCapture?

> `optional` **onDurationChangeCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2334

#### Inherited from

`ComponentPropsWithoutRef.onDurationChangeCapture`

***

### onEmptied?

> `optional` **onEmptied?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2335

#### Inherited from

`ComponentPropsWithoutRef.onEmptied`

***

### onEmptiedCapture?

> `optional` **onEmptiedCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2336

#### Inherited from

`ComponentPropsWithoutRef.onEmptiedCapture`

***

### onEncrypted?

> `optional` **onEncrypted?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2337

#### Inherited from

`ComponentPropsWithoutRef.onEncrypted`

***

### onEncryptedCapture?

> `optional` **onEncryptedCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2338

#### Inherited from

`ComponentPropsWithoutRef.onEncryptedCapture`

***

### onEnded?

> `optional` **onEnded?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2339

#### Inherited from

`ComponentPropsWithoutRef.onEnded`

***

### onEndedCapture?

> `optional` **onEndedCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2340

#### Inherited from

`ComponentPropsWithoutRef.onEndedCapture`

***

### onError?

> `optional` **onError?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2313

#### Inherited from

`ComponentPropsWithoutRef.onError`

***

### onErrorCapture?

> `optional` **onErrorCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2314

#### Inherited from

`ComponentPropsWithoutRef.onErrorCapture`

***

### onFocus?

> `optional` **onFocus?**: `FocusEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2291

#### Inherited from

`ComponentPropsWithoutRef.onFocus`

***

### onFocusCapture?

> `optional` **onFocusCapture?**: `FocusEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2292

#### Inherited from

`ComponentPropsWithoutRef.onFocusCapture`

***

### onGotPointerCapture?

> `optional` **onGotPointerCapture?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2439

#### Inherited from

`ComponentPropsWithoutRef.onGotPointerCapture`

***

### onGotPointerCaptureCapture?

> `optional` **onGotPointerCaptureCapture?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2440

#### Inherited from

`ComponentPropsWithoutRef.onGotPointerCaptureCapture`

***

### onInput?

> `optional` **onInput?**: `InputEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2301

#### Inherited from

`ComponentPropsWithoutRef.onInput`

***

### onInputCapture?

> `optional` **onInputCapture?**: `InputEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2302

#### Inherited from

`ComponentPropsWithoutRef.onInputCapture`

***

### onInvalid?

> `optional` **onInvalid?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2307

#### Inherited from

`ComponentPropsWithoutRef.onInvalid`

***

### onInvalidCapture?

> `optional` **onInvalidCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2308

#### Inherited from

`ComponentPropsWithoutRef.onInvalidCapture`

***

### onKeyDown?

> `optional` **onKeyDown?**: `KeyboardEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2317

#### Inherited from

`ComponentPropsWithoutRef.onKeyDown`

***

### onKeyDownCapture?

> `optional` **onKeyDownCapture?**: `KeyboardEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2318

#### Inherited from

`ComponentPropsWithoutRef.onKeyDownCapture`

***

### ~~onKeyPress?~~

> `optional` **onKeyPress?**: `KeyboardEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2320

#### Deprecated

Use `onKeyUp` or `onKeyDown` instead

#### Inherited from

`ComponentPropsWithoutRef.onKeyPress`

***

### ~~onKeyPressCapture?~~

> `optional` **onKeyPressCapture?**: `KeyboardEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2322

#### Deprecated

Use `onKeyUpCapture` or `onKeyDownCapture` instead

#### Inherited from

`ComponentPropsWithoutRef.onKeyPressCapture`

***

### onKeyUp?

> `optional` **onKeyUp?**: `KeyboardEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2323

#### Inherited from

`ComponentPropsWithoutRef.onKeyUp`

***

### onKeyUpCapture?

> `optional` **onKeyUpCapture?**: `KeyboardEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2324

#### Inherited from

`ComponentPropsWithoutRef.onKeyUpCapture`

***

### onLoad?

> `optional` **onLoad?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2311

#### Inherited from

`ComponentPropsWithoutRef.onLoad`

***

### onLoadCapture?

> `optional` **onLoadCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2312

#### Inherited from

`ComponentPropsWithoutRef.onLoadCapture`

***

### onLoadedData?

> `optional` **onLoadedData?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2341

#### Inherited from

`ComponentPropsWithoutRef.onLoadedData`

***

### onLoadedDataCapture?

> `optional` **onLoadedDataCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2342

#### Inherited from

`ComponentPropsWithoutRef.onLoadedDataCapture`

***

### onLoadedMetadata?

> `optional` **onLoadedMetadata?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2343

#### Inherited from

`ComponentPropsWithoutRef.onLoadedMetadata`

***

### onLoadedMetadataCapture?

> `optional` **onLoadedMetadataCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2344

#### Inherited from

`ComponentPropsWithoutRef.onLoadedMetadataCapture`

***

### onLoadStart?

> `optional` **onLoadStart?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2345

#### Inherited from

`ComponentPropsWithoutRef.onLoadStart`

***

### onLoadStartCapture?

> `optional` **onLoadStartCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2346

#### Inherited from

`ComponentPropsWithoutRef.onLoadStartCapture`

***

### onLostPointerCapture?

> `optional` **onLostPointerCapture?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2441

#### Inherited from

`ComponentPropsWithoutRef.onLostPointerCapture`

***

### onLostPointerCaptureCapture?

> `optional` **onLostPointerCaptureCapture?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2442

#### Inherited from

`ComponentPropsWithoutRef.onLostPointerCaptureCapture`

***

### onMouseDown?

> `optional` **onMouseDown?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2397

#### Inherited from

`ComponentPropsWithoutRef.onMouseDown`

***

### onMouseDownCapture?

> `optional` **onMouseDownCapture?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2398

#### Inherited from

`ComponentPropsWithoutRef.onMouseDownCapture`

***

### onMouseEnter?

> `optional` **onMouseEnter?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2399

#### Inherited from

`ComponentPropsWithoutRef.onMouseEnter`

***

### onMouseLeave?

> `optional` **onMouseLeave?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2400

#### Inherited from

`ComponentPropsWithoutRef.onMouseLeave`

***

### onMouseMove?

> `optional` **onMouseMove?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2401

#### Inherited from

`ComponentPropsWithoutRef.onMouseMove`

***

### onMouseMoveCapture?

> `optional` **onMouseMoveCapture?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2402

#### Inherited from

`ComponentPropsWithoutRef.onMouseMoveCapture`

***

### onMouseOut?

> `optional` **onMouseOut?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2403

#### Inherited from

`ComponentPropsWithoutRef.onMouseOut`

***

### onMouseOutCapture?

> `optional` **onMouseOutCapture?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2404

#### Inherited from

`ComponentPropsWithoutRef.onMouseOutCapture`

***

### onMouseOver?

> `optional` **onMouseOver?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2405

#### Inherited from

`ComponentPropsWithoutRef.onMouseOver`

***

### onMouseOverCapture?

> `optional` **onMouseOverCapture?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2406

#### Inherited from

`ComponentPropsWithoutRef.onMouseOverCapture`

***

### onMouseUp?

> `optional` **onMouseUp?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2407

#### Inherited from

`ComponentPropsWithoutRef.onMouseUp`

***

### onMouseUpCapture?

> `optional` **onMouseUpCapture?**: `MouseEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2408

#### Inherited from

`ComponentPropsWithoutRef.onMouseUpCapture`

***

### onPaste?

> `optional` **onPaste?**: `ClipboardEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2279

#### Inherited from

`ComponentPropsWithoutRef.onPaste`

***

### onPasteCapture?

> `optional` **onPasteCapture?**: `ClipboardEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2280

#### Inherited from

`ComponentPropsWithoutRef.onPasteCapture`

***

### onPause?

> `optional` **onPause?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2347

#### Inherited from

`ComponentPropsWithoutRef.onPause`

***

### onPauseCapture?

> `optional` **onPauseCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2348

#### Inherited from

`ComponentPropsWithoutRef.onPauseCapture`

***

### onPlay?

> `optional` **onPlay?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2349

#### Inherited from

`ComponentPropsWithoutRef.onPlay`

***

### onPlayCapture?

> `optional` **onPlayCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2350

#### Inherited from

`ComponentPropsWithoutRef.onPlayCapture`

***

### onPlaying?

> `optional` **onPlaying?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2351

#### Inherited from

`ComponentPropsWithoutRef.onPlaying`

***

### onPlayingCapture?

> `optional` **onPlayingCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2352

#### Inherited from

`ComponentPropsWithoutRef.onPlayingCapture`

***

### onPointerCancel?

> `optional` **onPointerCancel?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2431

#### Inherited from

`ComponentPropsWithoutRef.onPointerCancel`

***

### onPointerCancelCapture?

> `optional` **onPointerCancelCapture?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2432

#### Inherited from

`ComponentPropsWithoutRef.onPointerCancelCapture`

***

### onPointerDown?

> `optional` **onPointerDown?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2425

#### Inherited from

`ComponentPropsWithoutRef.onPointerDown`

***

### onPointerDownCapture?

> `optional` **onPointerDownCapture?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2426

#### Inherited from

`ComponentPropsWithoutRef.onPointerDownCapture`

***

### onPointerEnter?

> `optional` **onPointerEnter?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2433

#### Inherited from

`ComponentPropsWithoutRef.onPointerEnter`

***

### onPointerLeave?

> `optional` **onPointerLeave?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2434

#### Inherited from

`ComponentPropsWithoutRef.onPointerLeave`

***

### onPointerMove?

> `optional` **onPointerMove?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2427

#### Inherited from

`ComponentPropsWithoutRef.onPointerMove`

***

### onPointerMoveCapture?

> `optional` **onPointerMoveCapture?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2428

#### Inherited from

`ComponentPropsWithoutRef.onPointerMoveCapture`

***

### onPointerOut?

> `optional` **onPointerOut?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2437

#### Inherited from

`ComponentPropsWithoutRef.onPointerOut`

***

### onPointerOutCapture?

> `optional` **onPointerOutCapture?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2438

#### Inherited from

`ComponentPropsWithoutRef.onPointerOutCapture`

***

### onPointerOver?

> `optional` **onPointerOver?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2435

#### Inherited from

`ComponentPropsWithoutRef.onPointerOver`

***

### onPointerOverCapture?

> `optional` **onPointerOverCapture?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2436

#### Inherited from

`ComponentPropsWithoutRef.onPointerOverCapture`

***

### onPointerUp?

> `optional` **onPointerUp?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2429

#### Inherited from

`ComponentPropsWithoutRef.onPointerUp`

***

### onPointerUpCapture?

> `optional` **onPointerUpCapture?**: `PointerEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2430

#### Inherited from

`ComponentPropsWithoutRef.onPointerUpCapture`

***

### onProgress?

> `optional` **onProgress?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2353

#### Inherited from

`ComponentPropsWithoutRef.onProgress`

***

### onProgressCapture?

> `optional` **onProgressCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2354

#### Inherited from

`ComponentPropsWithoutRef.onProgressCapture`

***

### onRateChange?

> `optional` **onRateChange?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2355

#### Inherited from

`ComponentPropsWithoutRef.onRateChange`

***

### onRateChangeCapture?

> `optional` **onRateChangeCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2356

#### Inherited from

`ComponentPropsWithoutRef.onRateChangeCapture`

***

### onReset?

> `optional` **onReset?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2303

#### Inherited from

`ComponentPropsWithoutRef.onReset`

***

### onResetCapture?

> `optional` **onResetCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2304

#### Inherited from

`ComponentPropsWithoutRef.onResetCapture`

***

### onScroll?

> `optional` **onScroll?**: `UIEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2445

#### Inherited from

`ComponentPropsWithoutRef.onScroll`

***

### onScrollCapture?

> `optional` **onScrollCapture?**: `UIEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2446

#### Inherited from

`ComponentPropsWithoutRef.onScrollCapture`

***

### onScrollEnd?

> `optional` **onScrollEnd?**: `UIEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2447

#### Inherited from

`ComponentPropsWithoutRef.onScrollEnd`

***

### onScrollEndCapture?

> `optional` **onScrollEndCapture?**: `UIEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2448

#### Inherited from

`ComponentPropsWithoutRef.onScrollEndCapture`

***

### onSeeked?

> `optional` **onSeeked?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2357

#### Inherited from

`ComponentPropsWithoutRef.onSeeked`

***

### onSeekedCapture?

> `optional` **onSeekedCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2358

#### Inherited from

`ComponentPropsWithoutRef.onSeekedCapture`

***

### onSeeking?

> `optional` **onSeeking?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2359

#### Inherited from

`ComponentPropsWithoutRef.onSeeking`

***

### onSeekingCapture?

> `optional` **onSeekingCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2360

#### Inherited from

`ComponentPropsWithoutRef.onSeekingCapture`

***

### onSelect?

> `optional` **onSelect?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2411

#### Inherited from

`ComponentPropsWithoutRef.onSelect`

***

### onSelectCapture?

> `optional` **onSelectCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2412

#### Inherited from

`ComponentPropsWithoutRef.onSelectCapture`

***

### onStalled?

> `optional` **onStalled?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2361

#### Inherited from

`ComponentPropsWithoutRef.onStalled`

***

### onStalledCapture?

> `optional` **onStalledCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2362

#### Inherited from

`ComponentPropsWithoutRef.onStalledCapture`

***

### onSubmit?

> `optional` **onSubmit?**: `SubmitEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2305

#### Inherited from

`ComponentPropsWithoutRef.onSubmit`

***

### onSubmitCapture?

> `optional` **onSubmitCapture?**: `SubmitEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2306

#### Inherited from

`ComponentPropsWithoutRef.onSubmitCapture`

***

### onSuspend?

> `optional` **onSuspend?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2363

#### Inherited from

`ComponentPropsWithoutRef.onSuspend`

***

### onSuspendCapture?

> `optional` **onSuspendCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2364

#### Inherited from

`ComponentPropsWithoutRef.onSuspendCapture`

***

### onTimeUpdate?

> `optional` **onTimeUpdate?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2365

#### Inherited from

`ComponentPropsWithoutRef.onTimeUpdate`

***

### onTimeUpdateCapture?

> `optional` **onTimeUpdateCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2366

#### Inherited from

`ComponentPropsWithoutRef.onTimeUpdateCapture`

***

### onToggle?

> `optional` **onToggle?**: `ToggleEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2463

#### Inherited from

`ComponentPropsWithoutRef.onToggle`

***

### onTouchCancel?

> `optional` **onTouchCancel?**: `TouchEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2415

#### Inherited from

`ComponentPropsWithoutRef.onTouchCancel`

***

### onTouchCancelCapture?

> `optional` **onTouchCancelCapture?**: `TouchEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2416

#### Inherited from

`ComponentPropsWithoutRef.onTouchCancelCapture`

***

### onTouchEnd?

> `optional` **onTouchEnd?**: `TouchEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2417

#### Inherited from

`ComponentPropsWithoutRef.onTouchEnd`

***

### onTouchEndCapture?

> `optional` **onTouchEndCapture?**: `TouchEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2418

#### Inherited from

`ComponentPropsWithoutRef.onTouchEndCapture`

***

### onTouchMove?

> `optional` **onTouchMove?**: `TouchEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2419

#### Inherited from

`ComponentPropsWithoutRef.onTouchMove`

***

### onTouchMoveCapture?

> `optional` **onTouchMoveCapture?**: `TouchEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2420

#### Inherited from

`ComponentPropsWithoutRef.onTouchMoveCapture`

***

### onTouchStart?

> `optional` **onTouchStart?**: `TouchEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2421

#### Inherited from

`ComponentPropsWithoutRef.onTouchStart`

***

### onTouchStartCapture?

> `optional` **onTouchStartCapture?**: `TouchEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2422

#### Inherited from

`ComponentPropsWithoutRef.onTouchStartCapture`

***

### onTransitionCancel?

> `optional` **onTransitionCancel?**: `TransitionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2467

#### Inherited from

`ComponentPropsWithoutRef.onTransitionCancel`

***

### onTransitionCancelCapture?

> `optional` **onTransitionCancelCapture?**: `TransitionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2468

#### Inherited from

`ComponentPropsWithoutRef.onTransitionCancelCapture`

***

### onTransitionEnd?

> `optional` **onTransitionEnd?**: `TransitionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2469

#### Inherited from

`ComponentPropsWithoutRef.onTransitionEnd`

***

### onTransitionEndCapture?

> `optional` **onTransitionEndCapture?**: `TransitionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2470

#### Inherited from

`ComponentPropsWithoutRef.onTransitionEndCapture`

***

### onTransitionRun?

> `optional` **onTransitionRun?**: `TransitionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2471

#### Inherited from

`ComponentPropsWithoutRef.onTransitionRun`

***

### onTransitionRunCapture?

> `optional` **onTransitionRunCapture?**: `TransitionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2472

#### Inherited from

`ComponentPropsWithoutRef.onTransitionRunCapture`

***

### onTransitionStart?

> `optional` **onTransitionStart?**: `TransitionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2473

#### Inherited from

`ComponentPropsWithoutRef.onTransitionStart`

***

### onTransitionStartCapture?

> `optional` **onTransitionStartCapture?**: `TransitionEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2474

#### Inherited from

`ComponentPropsWithoutRef.onTransitionStartCapture`

***

### onVolumeChange?

> `optional` **onVolumeChange?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2367

#### Inherited from

`ComponentPropsWithoutRef.onVolumeChange`

***

### onVolumeChangeCapture?

> `optional` **onVolumeChangeCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2368

#### Inherited from

`ComponentPropsWithoutRef.onVolumeChangeCapture`

***

### onWaiting?

> `optional` **onWaiting?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2369

#### Inherited from

`ComponentPropsWithoutRef.onWaiting`

***

### onWaitingCapture?

> `optional` **onWaitingCapture?**: `ReactEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2370

#### Inherited from

`ComponentPropsWithoutRef.onWaitingCapture`

***

### onWheel?

> `optional` **onWheel?**: `WheelEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2451

#### Inherited from

`ComponentPropsWithoutRef.onWheel`

***

### onWheelCapture?

> `optional` **onWheelCapture?**: `WheelEventHandler`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:2452

#### Inherited from

`ComponentPropsWithoutRef.onWheelCapture`

***

### opacity?

> `optional` **opacity?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3771

#### Inherited from

`ComponentPropsWithoutRef.opacity`

***

### operator?

> `optional` **operator?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3772

#### Inherited from

`ComponentPropsWithoutRef.operator`

***

### order?

> `optional` **order?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3773

#### Inherited from

`ComponentPropsWithoutRef.order`

***

### orient?

> `optional` **orient?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3774

#### Inherited from

`ComponentPropsWithoutRef.orient`

***

### orientation?

> `optional` **orientation?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3775

#### Inherited from

`ComponentPropsWithoutRef.orientation`

***

### origin?

> `optional` **origin?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3776

#### Inherited from

`ComponentPropsWithoutRef.origin`

***

### overflow?

> `optional` **overflow?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3777

#### Inherited from

`ComponentPropsWithoutRef.overflow`

***

### overlinePosition?

> `optional` **overlinePosition?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3778

#### Inherited from

`ComponentPropsWithoutRef.overlinePosition`

***

### overlineThickness?

> `optional` **overlineThickness?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3779

#### Inherited from

`ComponentPropsWithoutRef.overlineThickness`

***

### paintOrder?

> `optional` **paintOrder?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3780

#### Inherited from

`ComponentPropsWithoutRef.paintOrder`

***

### panose1?

> `optional` **panose1?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3781

#### Inherited from

`ComponentPropsWithoutRef.panose1`

***

### part?

> `optional` **part?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3611

#### Inherited from

`ComponentPropsWithoutRef.part`

***

### path?

> `optional` **path?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3782

#### Inherited from

`ComponentPropsWithoutRef.path`

***

### pathLength?

> `optional` **pathLength?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3783

#### Inherited from

`ComponentPropsWithoutRef.pathLength`

***

### patternContentUnits?

> `optional` **patternContentUnits?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3784

#### Inherited from

`ComponentPropsWithoutRef.patternContentUnits`

***

### patternTransform?

> `optional` **patternTransform?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3785

#### Inherited from

`ComponentPropsWithoutRef.patternTransform`

***

### patternUnits?

> `optional` **patternUnits?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3786

#### Inherited from

`ComponentPropsWithoutRef.patternUnits`

***

### pointerEvents?

> `optional` **pointerEvents?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3787

#### Inherited from

`ComponentPropsWithoutRef.pointerEvents`

***

### points?

> `optional` **points?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3788

#### Inherited from

`ComponentPropsWithoutRef.points`

***

### pointsAtX?

> `optional` **pointsAtX?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3789

#### Inherited from

`ComponentPropsWithoutRef.pointsAtX`

***

### pointsAtY?

> `optional` **pointsAtY?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3790

#### Inherited from

`ComponentPropsWithoutRef.pointsAtY`

***

### pointsAtZ?

> `optional` **pointsAtZ?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3791

#### Inherited from

`ComponentPropsWithoutRef.pointsAtZ`

***

### preserveAlpha?

> `optional` **preserveAlpha?**: `Booleanish`

Defined in: node\_modules/@types/react/index.d.ts:3792

#### Inherited from

`ComponentPropsWithoutRef.preserveAlpha`

***

### preserveAspectRatio?

> `optional` **preserveAspectRatio?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3793

#### Inherited from

`ComponentPropsWithoutRef.preserveAspectRatio`

***

### primitiveUnits?

> `optional` **primitiveUnits?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3794

#### Inherited from

`ComponentPropsWithoutRef.primitiveUnits`

***

### r?

> `optional` **r?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3795

#### Inherited from

`ComponentPropsWithoutRef.r`

***

### radius?

> `optional` **radius?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3796

#### Inherited from

`ComponentPropsWithoutRef.radius`

***

### ref?

> `optional` **ref?**: `Ref`\<`SVGSVGElement`\>

Defined in: node\_modules/@types/react/index.d.ts:301

Allows getting a ref to the component instance.
Once the component unmounts, React will set `ref.current` to `null`
(or call the ref with `null` if you passed a callback ref).

#### See

[React Docs](https://react.dev/learn/referencing-values-with-refs#refs-and-the-dom)

#### Inherited from

`RefAttributes.ref`

***

### refX?

> `optional` **refX?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3797

#### Inherited from

`ComponentPropsWithoutRef.refX`

***

### refY?

> `optional` **refY?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3798

#### Inherited from

`ComponentPropsWithoutRef.refY`

***

### renderingIntent?

> `optional` **renderingIntent?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3799

#### Inherited from

`ComponentPropsWithoutRef.renderingIntent`

***

### repeatCount?

> `optional` **repeatCount?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3800

#### Inherited from

`ComponentPropsWithoutRef.repeatCount`

***

### repeatDur?

> `optional` **repeatDur?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3801

#### Inherited from

`ComponentPropsWithoutRef.repeatDur`

***

### requiredExtensions?

> `optional` **requiredExtensions?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3802

#### Inherited from

`ComponentPropsWithoutRef.requiredExtensions`

***

### requiredFeatures?

> `optional` **requiredFeatures?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3803

#### Inherited from

`ComponentPropsWithoutRef.requiredFeatures`

***

### restart?

> `optional` **restart?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3804

#### Inherited from

`ComponentPropsWithoutRef.restart`

***

### result?

> `optional` **result?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3805

#### Inherited from

`ComponentPropsWithoutRef.result`

***

### role?

> `optional` **role?**: `AriaRole`

Defined in: node\_modules/@types/react/index.d.ts:3619

#### Inherited from

`ComponentPropsWithoutRef.role`

***

### rotate?

> `optional` **rotate?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3806

#### Inherited from

`ComponentPropsWithoutRef.rotate`

***

### rx?

> `optional` **rx?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3807

#### Inherited from

`ComponentPropsWithoutRef.rx`

***

### ry?

> `optional` **ry?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3808

#### Inherited from

`ComponentPropsWithoutRef.ry`

***

### scale?

> `optional` **scale?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3809

#### Inherited from

`ComponentPropsWithoutRef.scale`

***

### seed?

> `optional` **seed?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3810

#### Inherited from

`ComponentPropsWithoutRef.seed`

***

### shapeRendering?

> `optional` **shapeRendering?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3811

#### Inherited from

`ComponentPropsWithoutRef.shapeRendering`

***

### size?

> `optional` **size?**: `string` \| `number`

Defined in: node\_modules/@phosphor-icons/react/dist/lib/types.d.ts:6

***

### slope?

> `optional` **slope?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3812

#### Inherited from

`ComponentPropsWithoutRef.slope`

***

### slot?

> `optional` **slot?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3612

#### Inherited from

`ComponentPropsWithoutRef.slot`

***

### spacing?

> `optional` **spacing?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3813

#### Inherited from

`ComponentPropsWithoutRef.spacing`

***

### specularConstant?

> `optional` **specularConstant?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3814

#### Inherited from

`ComponentPropsWithoutRef.specularConstant`

***

### specularExponent?

> `optional` **specularExponent?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3815

#### Inherited from

`ComponentPropsWithoutRef.specularExponent`

***

### speed?

> `optional` **speed?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3816

#### Inherited from

`ComponentPropsWithoutRef.speed`

***

### spreadMethod?

> `optional` **spreadMethod?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3817

#### Inherited from

`ComponentPropsWithoutRef.spreadMethod`

***

### startOffset?

> `optional` **startOffset?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3818

#### Inherited from

`ComponentPropsWithoutRef.startOffset`

***

### stdDeviation?

> `optional` **stdDeviation?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3819

#### Inherited from

`ComponentPropsWithoutRef.stdDeviation`

***

### stemh?

> `optional` **stemh?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3820

#### Inherited from

`ComponentPropsWithoutRef.stemh`

***

### stemv?

> `optional` **stemv?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3821

#### Inherited from

`ComponentPropsWithoutRef.stemv`

***

### stitchTiles?

> `optional` **stitchTiles?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3822

#### Inherited from

`ComponentPropsWithoutRef.stitchTiles`

***

### stopColor?

> `optional` **stopColor?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3823

#### Inherited from

`ComponentPropsWithoutRef.stopColor`

***

### stopOpacity?

> `optional` **stopOpacity?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3824

#### Inherited from

`ComponentPropsWithoutRef.stopOpacity`

***

### strikethroughPosition?

> `optional` **strikethroughPosition?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3825

#### Inherited from

`ComponentPropsWithoutRef.strikethroughPosition`

***

### strikethroughThickness?

> `optional` **strikethroughThickness?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3826

#### Inherited from

`ComponentPropsWithoutRef.strikethroughThickness`

***

### string?

> `optional` **string?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3827

#### Inherited from

`ComponentPropsWithoutRef.string`

***

### stroke?

> `optional` **stroke?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3828

#### Inherited from

`ComponentPropsWithoutRef.stroke`

***

### strokeDasharray?

> `optional` **strokeDasharray?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3829

#### Inherited from

`ComponentPropsWithoutRef.strokeDasharray`

***

### strokeDashoffset?

> `optional` **strokeDashoffset?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3830

#### Inherited from

`ComponentPropsWithoutRef.strokeDashoffset`

***

### strokeLinecap?

> `optional` **strokeLinecap?**: `"inherit"` \| `"round"` \| `"butt"` \| `"square"`

Defined in: node\_modules/@types/react/index.d.ts:3831

#### Inherited from

`ComponentPropsWithoutRef.strokeLinecap`

***

### strokeLinejoin?

> `optional` **strokeLinejoin?**: `"inherit"` \| `"round"` \| `"bevel"` \| `"miter"`

Defined in: node\_modules/@types/react/index.d.ts:3832

#### Inherited from

`ComponentPropsWithoutRef.strokeLinejoin`

***

### strokeMiterlimit?

> `optional` **strokeMiterlimit?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3833

#### Inherited from

`ComponentPropsWithoutRef.strokeMiterlimit`

***

### strokeOpacity?

> `optional` **strokeOpacity?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3834

#### Inherited from

`ComponentPropsWithoutRef.strokeOpacity`

***

### strokeWidth?

> `optional` **strokeWidth?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3835

#### Inherited from

`ComponentPropsWithoutRef.strokeWidth`

***

### style?

> `optional` **style?**: `CSSProperties`

Defined in: node\_modules/@types/react/index.d.ts:3613

#### Inherited from

`ComponentPropsWithoutRef.style`

***

### suppressHydrationWarning?

> `optional` **suppressHydrationWarning?**: `boolean`

Defined in: node\_modules/@types/react/index.d.ts:3596

#### Inherited from

`ComponentPropsWithoutRef.suppressHydrationWarning`

***

### surfaceScale?

> `optional` **surfaceScale?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3836

#### Inherited from

`ComponentPropsWithoutRef.surfaceScale`

***

### systemLanguage?

> `optional` **systemLanguage?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3837

#### Inherited from

`ComponentPropsWithoutRef.systemLanguage`

***

### tabIndex?

> `optional` **tabIndex?**: `number`

Defined in: node\_modules/@types/react/index.d.ts:3620

#### Inherited from

`ComponentPropsWithoutRef.tabIndex`

***

### tableValues?

> `optional` **tableValues?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3838

#### Inherited from

`ComponentPropsWithoutRef.tableValues`

***

### target?

> `optional` **target?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3614

#### Inherited from

`ComponentPropsWithoutRef.target`

***

### targetX?

> `optional` **targetX?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3839

#### Inherited from

`ComponentPropsWithoutRef.targetX`

***

### targetY?

> `optional` **targetY?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3840

#### Inherited from

`ComponentPropsWithoutRef.targetY`

***

### textAnchor?

> `optional` **textAnchor?**: `"inherit"` \| `"end"` \| `"start"` \| `"middle"`

Defined in: node\_modules/@types/react/index.d.ts:3841

#### Inherited from

`ComponentPropsWithoutRef.textAnchor`

***

### textDecoration?

> `optional` **textDecoration?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3842

#### Inherited from

`ComponentPropsWithoutRef.textDecoration`

***

### textLength?

> `optional` **textLength?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3843

#### Inherited from

`ComponentPropsWithoutRef.textLength`

***

### textRendering?

> `optional` **textRendering?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3844

#### Inherited from

`ComponentPropsWithoutRef.textRendering`

***

### to?

> `optional` **to?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3845

#### Inherited from

`ComponentPropsWithoutRef.to`

***

### transform?

> `optional` **transform?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3846

#### Inherited from

`ComponentPropsWithoutRef.transform`

***

### type?

> `optional` **type?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3615

#### Inherited from

`ComponentPropsWithoutRef.type`

***

### u1?

> `optional` **u1?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3847

#### Inherited from

`ComponentPropsWithoutRef.u1`

***

### u2?

> `optional` **u2?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3848

#### Inherited from

`ComponentPropsWithoutRef.u2`

***

### underlinePosition?

> `optional` **underlinePosition?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3849

#### Inherited from

`ComponentPropsWithoutRef.underlinePosition`

***

### underlineThickness?

> `optional` **underlineThickness?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3850

#### Inherited from

`ComponentPropsWithoutRef.underlineThickness`

***

### unicode?

> `optional` **unicode?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3851

#### Inherited from

`ComponentPropsWithoutRef.unicode`

***

### unicodeBidi?

> `optional` **unicodeBidi?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3852

#### Inherited from

`ComponentPropsWithoutRef.unicodeBidi`

***

### unicodeRange?

> `optional` **unicodeRange?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3853

#### Inherited from

`ComponentPropsWithoutRef.unicodeRange`

***

### unitsPerEm?

> `optional` **unitsPerEm?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3854

#### Inherited from

`ComponentPropsWithoutRef.unitsPerEm`

***

### vAlphabetic?

> `optional` **vAlphabetic?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3855

#### Inherited from

`ComponentPropsWithoutRef.vAlphabetic`

***

### values?

> `optional` **values?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3856

#### Inherited from

`ComponentPropsWithoutRef.values`

***

### vectorEffect?

> `optional` **vectorEffect?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3857

#### Inherited from

`ComponentPropsWithoutRef.vectorEffect`

***

### version?

> `optional` **version?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3858

#### Inherited from

`ComponentPropsWithoutRef.version`

***

### vertAdvY?

> `optional` **vertAdvY?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3859

#### Inherited from

`ComponentPropsWithoutRef.vertAdvY`

***

### vertOriginX?

> `optional` **vertOriginX?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3860

#### Inherited from

`ComponentPropsWithoutRef.vertOriginX`

***

### vertOriginY?

> `optional` **vertOriginY?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3861

#### Inherited from

`ComponentPropsWithoutRef.vertOriginY`

***

### vHanging?

> `optional` **vHanging?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3862

#### Inherited from

`ComponentPropsWithoutRef.vHanging`

***

### vIdeographic?

> `optional` **vIdeographic?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3863

#### Inherited from

`ComponentPropsWithoutRef.vIdeographic`

***

### viewBox?

> `optional` **viewBox?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3864

#### Inherited from

`ComponentPropsWithoutRef.viewBox`

***

### viewTarget?

> `optional` **viewTarget?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3865

#### Inherited from

`ComponentPropsWithoutRef.viewTarget`

***

### visibility?

> `optional` **visibility?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3866

#### Inherited from

`ComponentPropsWithoutRef.visibility`

***

### vMathematical?

> `optional` **vMathematical?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3867

#### Inherited from

`ComponentPropsWithoutRef.vMathematical`

***

### weight?

> `optional` **weight?**: [`IconWeight`](../type-aliases/IconWeight.md)

Defined in: node\_modules/@phosphor-icons/react/dist/lib/types.d.ts:7

***

### width?

> `optional` **width?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3616

#### Inherited from

`ComponentPropsWithoutRef.width`

***

### widths?

> `optional` **widths?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3868

#### Inherited from

`ComponentPropsWithoutRef.widths`

***

### wordSpacing?

> `optional` **wordSpacing?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3869

#### Inherited from

`ComponentPropsWithoutRef.wordSpacing`

***

### writingMode?

> `optional` **writingMode?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3870

#### Inherited from

`ComponentPropsWithoutRef.writingMode`

***

### x?

> `optional` **x?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3873

#### Inherited from

`ComponentPropsWithoutRef.x`

***

### x1?

> `optional` **x1?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3871

#### Inherited from

`ComponentPropsWithoutRef.x1`

***

### x2?

> `optional` **x2?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3872

#### Inherited from

`ComponentPropsWithoutRef.x2`

***

### xChannelSelector?

> `optional` **xChannelSelector?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3874

#### Inherited from

`ComponentPropsWithoutRef.xChannelSelector`

***

### xHeight?

> `optional` **xHeight?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3875

#### Inherited from

`ComponentPropsWithoutRef.xHeight`

***

### xlinkActuate?

> `optional` **xlinkActuate?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3876

#### Inherited from

`ComponentPropsWithoutRef.xlinkActuate`

***

### xlinkArcrole?

> `optional` **xlinkArcrole?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3877

#### Inherited from

`ComponentPropsWithoutRef.xlinkArcrole`

***

### xlinkHref?

> `optional` **xlinkHref?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3878

#### Inherited from

`ComponentPropsWithoutRef.xlinkHref`

***

### xlinkRole?

> `optional` **xlinkRole?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3879

#### Inherited from

`ComponentPropsWithoutRef.xlinkRole`

***

### xlinkShow?

> `optional` **xlinkShow?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3880

#### Inherited from

`ComponentPropsWithoutRef.xlinkShow`

***

### xlinkTitle?

> `optional` **xlinkTitle?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3881

#### Inherited from

`ComponentPropsWithoutRef.xlinkTitle`

***

### xlinkType?

> `optional` **xlinkType?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3882

#### Inherited from

`ComponentPropsWithoutRef.xlinkType`

***

### xmlBase?

> `optional` **xmlBase?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3883

#### Inherited from

`ComponentPropsWithoutRef.xmlBase`

***

### xmlLang?

> `optional` **xmlLang?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3884

#### Inherited from

`ComponentPropsWithoutRef.xmlLang`

***

### xmlns?

> `optional` **xmlns?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3885

#### Inherited from

`ComponentPropsWithoutRef.xmlns`

***

### xmlnsXlink?

> `optional` **xmlnsXlink?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3886

#### Inherited from

`ComponentPropsWithoutRef.xmlnsXlink`

***

### xmlSpace?

> `optional` **xmlSpace?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3887

#### Inherited from

`ComponentPropsWithoutRef.xmlSpace`

***

### y?

> `optional` **y?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3890

#### Inherited from

`ComponentPropsWithoutRef.y`

***

### y1?

> `optional` **y1?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3888

#### Inherited from

`ComponentPropsWithoutRef.y1`

***

### y2?

> `optional` **y2?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3889

#### Inherited from

`ComponentPropsWithoutRef.y2`

***

### yChannelSelector?

> `optional` **yChannelSelector?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3891

#### Inherited from

`ComponentPropsWithoutRef.yChannelSelector`

***

### z?

> `optional` **z?**: `string` \| `number`

Defined in: node\_modules/@types/react/index.d.ts:3892

#### Inherited from

`ComponentPropsWithoutRef.z`

***

### zoomAndPan?

> `optional` **zoomAndPan?**: `string`

Defined in: node\_modules/@types/react/index.d.ts:3893

#### Inherited from

`ComponentPropsWithoutRef.zoomAndPan`
