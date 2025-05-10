# TRMNL Plugin Development Guide

## Overview
TRMNL is a terminal-based display system that allows for creating custom plugins to display information on terminal screens. This guide covers the essential aspects of developing plugins for TRMNL.

## Basic Structure
A TRMNL plugin consists of:
1. HTML template file
2. Required CSS/JS includes
3. Liquid templating for dynamic content
4. Custom styling

## Required Elements
```html
<!-- Required CSS and JS -->
<link rel="stylesheet" href="https://usetrmnl.com/css/latest/plugins.css">
<script src="https://usetrmnl.com/js/latest/plugins.js"></script>

<!-- Basic TRMNL structure -->
<body class="environment trmnl">
  <div class="screen">
    <div class="view view--full">
      <!-- Content goes here -->
    </div>
  </div>
</body>
```

## TRMNL System Variables
TRMNL provides several system variables for use in templates:

- `trmnl.system.timestamp_utc`: Current UTC timestamp
- `trmnl.user.utc_offset`: User's timezone offset in seconds
- `trmnl.system.version`: TRMNL version
- `trmnl.user.timezone`: User's timezone

## Time and Date Handling

### Timezone Management
TRMNL handles timezones through the `trmnl.user.utc_offset` variable, which provides the offset in seconds from UTC. Always use this for time calculations:

```liquid
{% assign local_time = trmnl.system.timestamp_utc | plus: trmnl.user.utc_offset %}
```

### Date Formatting
Liquid provides several date format options:

```liquid
{{ timestamp | date: "%I:%M %p" }}  <!-- 12-hour format with AM/PM -->
{{ timestamp | date: "%H:%M" }}     <!-- 24-hour format -->
{{ timestamp | date: "%Y-%m-%d" }}  <!-- Full date -->
{{ timestamp | date: "%a, %b %d" }} <!-- Day, Month Date -->
```

### Time Calculations
For time differences and manipulations:

```liquid
<!-- Convert to Unix timestamp -->
{% assign timestamp = date_string | date: "%s" %}

<!-- Add time (in seconds) -->
{% assign future_time = timestamp | plus: 300 %}  <!-- Add 5 minutes -->

<!-- Calculate difference in minutes -->
{% assign minutes_diff = end_time | minus: start_time | divided_by: 60 %}

<!-- Round to nearest minute -->
{% assign rounded_minutes = minutes_diff | round %}
```

### Common Time Patterns

1. **Display relative time**:
```liquid
{% if minutes_diff <= 0 %}
  Arriving
{% elsif minutes_diff < 60 %}
  {{ minutes_diff }} min
{% else %}
  {{ minutes_diff | divided_by: 60 }}h {{ minutes_diff | modulo: 60 }}m
{% endif %}
```

2. **Format time ranges**:
```liquid
{% assign start = start_time | date: "%I:%M %p" %}
{% assign end = end_time | date: "%I:%M %p" %}
{{ start }} - {{ end }}
```

3. **Handle timezone conversions**:
```liquid
{% assign utc_time = local_time | minus: trmnl.user.utc_offset %}
```

## UI Framework Components

### Layout Structure
TRMNL uses a grid-based layout system:

```html
<div class="layout">
  <div class="columns">
    <div class="column">
      <!-- Content -->
    </div>
  </div>
</div>
```

### Common UI Elements

1. **Title Bar**:
```html
<div class="title_bar">
  <img class="image" src="path/to/icon.svg" />
  <span class="title">Plugin Title</span>
  <span class="instance">Instance Name</span>
</div>
```

2. **Sections**:
```html
<div class="section">
  <span class="label label--underline">Section Title</span>
  <!-- Section content -->
</div>
```

3. **Content Areas**:
```html
<div class="content content--center">
  <!-- Centered content -->
</div>
<div class="content content--left">
  <!-- Left-aligned content -->
</div>
```

### Styling Classes

1. **Text Styling**:
```html
<span class="title">Large Title</span>
<span class="label">Label Text</span>
<span class="text--muted">Muted Text</span>
```

2. **Layout Classes**:
```html
<div class="view view--full">Full View</div>
<div class="view view--split">Split View</div>
<div class="columns columns--2">Two Columns</div>
```

3. **Status Indicators**:
```html
<span class="status status--success">✓</span>
<span class="status status--warning">!</span>
<span class="status status--error">✗</span>
```

### Custom Styling
Add custom styles within the `<style>` tag:

```html
<style>
  .custom-class {
    /* Your styles */
  }
  
  /* Use TRMNL variables for consistency */
  .custom-element {
    color: var(--trmnl-text-color);
    background: var(--trmnl-bg-color);
  }
</style>
```

## API Integration
When integrating with external APIs:

1. Use the plugin's configuration to store API keys and endpoints
2. Handle API responses in the template using Liquid's JSON parsing
3. Implement error handling for API failures
4. Consider rate limiting and caching strategies

## Styling Guidelines
1. Use the provided TRMNL classes for consistent styling
2. Custom styles should be scoped to your plugin
3. Use responsive design principles
4. Consider dark/light mode compatibility

## Best Practices
1. **Error Handling**
   - Always provide fallback content
   - Display meaningful error messages
   - Log errors appropriately

2. **Performance**
   - Minimize API calls
   - Cache data when possible
   - Optimize template logic

3. **User Experience**
   - Clear loading states
   - Intuitive layout
   - Consistent styling

4. **Maintenance**
   - Document code thoroughly
   - Use meaningful variable names
   - Comment complex logic

## Common Patterns

### Status Indicators
```liquid
{% case status %}
  {% when 'ON_TIME' %}
    ✓
  {% when 'DELAYED' %}
    !
  {% when 'CANCELLED' %}
    ✗
  {% else %}
    ?
{% endcase %}
```

### Conditional Display
```liquid
{% if condition %}
  <!-- Content -->
{% else %}
  <!-- Fallback -->
{% endif %}
```

### Looping Through Data
```liquid
{% for item in data %}
  <!-- Process each item -->
{% endfor %}
```

## Testing
1. Test with different timezones
2. Verify error handling
3. Check responsive design
4. Validate API integration
5. Test update intervals

## Deployment
1. Package plugin files
2. Include documentation
3. Version control
4. Update mechanism

## Troubleshooting
Common issues and solutions:
1. Timezone mismatches
2. API rate limits
3. Template syntax errors
4. Styling conflicts

## Resources

### Essential Documentation
- TRMNL Documentation: https://usetrmnl.com/docs
- Liquid Documentation: https://shopify.github.io/liquid/
- TRMNL CSS Reference: https://usetrmnl.com/css/latest/plugins.css

### Required External Resources
When developing TRMNL plugins, the following resources should be provided:

1. **API Documentation**
   - API endpoint specifications
   - Authentication requirements
   - Rate limits
   - Response format examples
   - Error codes and handling

2. **Design Assets**
   - Brand guidelines
   - Icon sets
   - Color palettes
   - Font specifications

3. **Example Responses**
   - Sample API responses
   - Edge cases
   - Error scenarios

4. **Configuration Requirements**
   - Required API keys
   - Environment variables
   - Plugin settings

### Development Environment
For optimal development, provide:
1. Access to a TRMNL development instance
2. API test credentials
3. Sample data sets
4. Development tools configuration

### Testing Resources
1. Test accounts
2. Test API endpoints
3. Mock data generators
4. Timezone test cases

### Support Resources
1. TRMNL support contact
2. API provider support
3. Development team contacts
4. Issue tracking system

## Quick Reference

### Common API Patterns
```liquid
<!-- API Response Structure -->
{
  "data": [
    {
      "id": "string",
      "attributes": {
        "property": "value"
      },
      "relationships": {
        "related": {
          "data": {
            "id": "string",
            "type": "string"
          }
        }
      }
    }
  ]
}
```

### Time Format Reference
```
%I - 12-hour format (01-12)
%H - 24-hour format (00-23)
%M - Minutes (00-59)
%p - AM/PM
%a - Abbreviated weekday name
%b - Abbreviated month name
%d - Day of month (01-31)
%Y - Year with century
```

### Status Code Reference
```
200 - Success
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
429 - Too Many Requests
500 - Server Error
```

### Common CSS Variables
```css
--trmnl-text-color
--trmnl-bg-color
--trmnl-accent-color
--trmnl-error-color
--trmnl-warning-color
--trmnl-success-color
```

## Development Checklist
1. [ ] API integration configured
2. [ ] Timezone handling implemented
3. [ ] Error states handled
4. [ ] Loading states implemented
5. [ ] Responsive design verified
6. [ ] Dark/light mode tested
7. [ ] Documentation updated
8. [ ] Code commented
9. [ ] Performance optimized
10. [ ] Security reviewed 