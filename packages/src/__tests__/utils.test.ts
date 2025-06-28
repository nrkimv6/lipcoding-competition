import { isValidEmail, isStrongPassword, uniqueArray, slugify } from '../utils';

describe('Utility Functions', () => {
  describe('isValidEmail', () => {
    it('should return true for valid emails', () => {
      expect(isValidEmail('test@example.com')).toBe(true);
      expect(isValidEmail('user.name@domain.co.kr')).toBe(true);
    });

    it('should return false for invalid emails', () => {
      expect(isValidEmail('invalid-email')).toBe(false);
      expect(isValidEmail('test@')).toBe(false);
      expect(isValidEmail('@example.com')).toBe(false);
    });
  });

  describe('isStrongPassword', () => {
    it('should return true for strong passwords', () => {
      expect(isStrongPassword('StrongPass123!')).toBe(true);
      expect(isStrongPassword('Aa1@bcdefg')).toBe(true);
    });

    it('should return false for weak passwords', () => {
      expect(isStrongPassword('weak')).toBe(false);
      expect(isStrongPassword('nouppercaseornumbers')).toBe(false);
      expect(isStrongPassword('NOLOWERCASE123!')).toBe(false);
    });
  });

  describe('uniqueArray', () => {
    it('should remove duplicates from array', () => {
      expect(uniqueArray([1, 2, 2, 3, 3, 3])).toEqual([1, 2, 3]);
      expect(uniqueArray(['a', 'b', 'a', 'c'])).toEqual(['a', 'b', 'c']);
    });
  });

  describe('slugify', () => {
    it('should convert text to URL-friendly slug', () => {
      expect(slugify('Hello World!')).toBe('hello-world');
      expect(slugify('  React Developer  ')).toBe('react-developer');
      expect(slugify('JavaScript & TypeScript')).toBe('javascript-typescript');
    });
  });
});
